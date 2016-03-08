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

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import (UserLineRelation,
                                         LineExtensionRelation,
                                         LineEndpointSipRelation,
                                         LineEndpointSccpRelation,
                                         LineEndpointCustomRelation,
                                         LineDeviceRelation)


class LineRelation(object):

    def __init__(self, builder, line_id):
        self.line_id = line_id
        self.user_line = UserLineRelation(builder)
        self.line_extension = LineExtensionRelation(builder)
        self.line_endpoint_sip = LineEndpointSipRelation(builder)
        self.line_endpoint_sccp = LineEndpointSccpRelation(builder)
        self.line_endpoint_custom = LineEndpointCustomRelation(builder)
        self.line_device = LineDeviceRelation(builder)

    @extract_id
    def add_extension(self, extension_id):
        return self.line_extension.associate(self.line_id, extension_id)

    @extract_id
    def remove_extension(self, extension_id):
        return self.line_extension.dissociate(self.line_id, extension_id)

    def list_extensions(self):
        return self.line_extension.list_by_line(self.line_id)

    @extract_id
    def add_user(self, user_id):
        return self.user_line.associate(user_id, self.line_id)

    @extract_id
    def remove_user(self, user_id):
        return self.user_line.dissociate(user_id, self.line_id)

    def list_users(self):
        return self.user_line.list_by_line(self.line_id)

    @extract_id
    def add_endpoint_sip(self, endpoint_sip_id):
        return self.line_endpoint_sip.associate(self.line_id, endpoint_sip_id)

    @extract_id
    def remove_endpoint_sip(self, endpoint_sip_id):
        return self.line_endpoint_sip.dissociate(self.line_id, endpoint_sip_id)

    def get_endpoint_sip(self):
        return self.line_endpoint_sip.get_by_line(self.line_id)

    @extract_id
    def add_endpoint_sccp(self, endpoint_sccp_id):
        return self.line_endpoint_sccp.associate(self.line_id, endpoint_sccp_id)

    @extract_id
    def remove_endpoint_sccp(self, endpoint_sccp_id):
        return self.line_endpoint_sccp.dissociate(self.line_id, endpoint_sccp_id)

    def get_endpoint_sccp(self):
        return self.line_endpoint_sccp.get_by_line(self.line_id)

    @extract_id
    def add_endpoint_custom(self, endpoint_custom_id):
        return self.line_endpoint_custom.associate(self.line_id, endpoint_custom_id)

    @extract_id
    def remove_endpoint_custom(self, endpoint_custom_id):
        return self.line_endpoint_custom.dissociate(self.line_id, endpoint_custom_id)

    def get_endpoint_custom(self):
        return self.line_endpoint_custom.get_by_line(self.line_id)

    @extract_id
    def add_device(self, device_id):
        return self.line_device.associate(self.line_id, device_id)

    @extract_id
    def remove_device(self, device_id):
        return self.line_device.dissociate(self.line_id, device_id)

    def get_device(self):
        return self.line_device.get_by_line(self.line_id)


class LinesCommand(CRUDCommand):

    resource = 'lines'
    relation_cmd = LineRelation
