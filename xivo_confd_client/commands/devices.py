# -*- coding: utf-8 -*-

# Copyright (C) 2015-2016 Avencall
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

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.util import extract_id
from xivo_confd_client.util import url_join
from xivo_confd_client.relations import LineDeviceRelation


class DeviceRelation(object):

    def __init__(self, builder, device_id):
        self.device_id = device_id
        self.line_device = LineDeviceRelation(builder)

    @extract_id
    def add_line(self, line_id):
        return self.line_device.associate(line_id, self.device_id)

    @extract_id
    def remove_line(self, line_id):
        return self.line_device.dissociate(line_id, self.device_id)

    def list_lines(self):
        return self.line_device.list_by_device(self.device_id)


class DevicesCommand(CRUDCommand):

    resource = 'devices'
    relation_cmd = DeviceRelation

    @extract_id
    def autoprov(self, device_id):
        url = url_join(self.resource, device_id, 'autoprov')
        self.session.get(url)

    @extract_id
    def synchronize(self, device_id):
        url = url_join(self.resource, device_id, 'synchronize')
        self.session.get(url)
