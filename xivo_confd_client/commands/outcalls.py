# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
# Copyright (C) 2016 Proformatique Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import OutcallExtensionRelation, OutcallTrunkRelation


class OutcallRelation(object):

    def __init__(self, builder, outcall_id):
        self.outcall_id = outcall_id
        self.outcall_trunk = OutcallTrunkRelation(builder)
        self.outcall_extension = OutcallExtensionRelation(builder)

    def update_trunks(self, trunks):
        return self.outcall_trunk.associate(self.outcall_id, trunks)

    @extract_id
    def add_extension(self, extension_id, **kwargs):
        return self.outcall_extension.associate(self.outcall_id, extension_id, **kwargs)

    @extract_id
    def remove_extension(self, extension_id):
        return self.outcall_extension.dissociate(self.outcall_id, extension_id)


class OutcallsCommand(CRUDCommand):

    resource = 'outcalls'
    relation_cmd = OutcallRelation
