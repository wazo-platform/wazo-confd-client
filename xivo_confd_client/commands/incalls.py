# -*- coding: utf-8 -*-

# Copyright 2016-2017 The Wazo Authors  (see the AUTHORS file)
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
from xivo_confd_client.relations import IncallExtensionRelation, IncallScheduleRelation


class IncallRelation(object):

    def __init__(self, builder, incall_id):
        self.incall_id = incall_id
        self.incall_extension = IncallExtensionRelation(builder)
        self.incall_schedule = IncallScheduleRelation(builder)

    @extract_id
    def add_extension(self, extension_id):
        return self.incall_extension.associate(self.incall_id, extension_id)

    @extract_id
    def remove_extension(self, extension_id):
        return self.incall_extension.dissociate(self.incall_id, extension_id)

    @extract_id
    def add_schedule(self, schedule_id):
        return self.schedule.associate(self.incall_id, schedule_id)

    @extract_id
    def remove_schedule(self, schedule_id):
        return self.incall_schedule.dissociate(self.incall_id, schedule_id)


class IncallsCommand(CRUDCommand):

    resource = 'incalls'
    relation_cmd = IncallRelation
