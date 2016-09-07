# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
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
from xivo_confd_client.relations import (TrunkEndpointSipRelation,
                                         TrunkEndpointCustomRelation)


class TrunkRelation(object):

    def __init__(self, builder, trunk_id):
        self.trunk_id = trunk_id
        self.trunk_endpoint_sip = TrunkEndpointSipRelation(builder)
        self.trunk_endpoint_custom = TrunkEndpointCustomRelation(builder)

    @extract_id
    def add_endpoint_sip(self, endpoint_sip_id):
        return self.trunk_endpoint_sip.associate(self.trunk_id, endpoint_sip_id)

    @extract_id
    def remove_endpoint_sip(self, endpoint_sip_id):
        return self.trunk_endpoint_sip.dissociate(self.trunk_id, endpoint_sip_id)

    def get_endpoint_sip(self):
        return self.trunk_endpoint_sip.get_by_trunk(self.trunk_id)

    @extract_id
    def add_endpoint_custom(self, endpoint_custom_id):
        return self.trunk_endpoint_custom.associate(self.trunk_id, endpoint_custom_id)

    @extract_id
    def remove_endpoint_custom(self, endpoint_custom_id):
        return self.trunk_endpoint_custom.dissociate(self.trunk_id, endpoint_custom_id)

    def get_endpoint_custom(self):
        return self.trunk_endpoint_custom.get_by_trunk(self.trunk_id)


class TrunksCommand(CRUDCommand):

    resource = 'trunks'
    relation_cmd = TrunkRelation
