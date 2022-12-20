# Copyright 2015-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.util import extract_id
from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import (
    LineApplicationRelation,
    LineDeviceRelation,
    LineEndpointCustomRelation,
    LineEndpointSccpRelation,
    LineEndpointSipRelation,
    LineExtensionRelation,
    UserLineRelation,
)


class LineRelation:
    def __init__(self, builder, line_id):
        self.line_id = line_id
        self.user_line = UserLineRelation(builder)
        self.line_application = LineApplicationRelation(builder)
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

    @extract_id
    def add_user(self, user_id):
        return self.user_line.associate(user_id, self.line_id)

    @extract_id
    def remove_user(self, user_id):
        return self.user_line.dissociate(user_id, self.line_id)

    @extract_id
    def add_endpoint_sip(self, endpoint_sip_id):
        return self.line_endpoint_sip.associate(self.line_id, endpoint_sip_id)

    @extract_id
    def remove_endpoint_sip(self, endpoint_sip_id):
        return self.line_endpoint_sip.dissociate(self.line_id, endpoint_sip_id)

    @extract_id
    def add_endpoint_sccp(self, endpoint_sccp_id):
        return self.line_endpoint_sccp.associate(self.line_id, endpoint_sccp_id)

    @extract_id
    def remove_endpoint_sccp(self, endpoint_sccp_id):
        return self.line_endpoint_sccp.dissociate(self.line_id, endpoint_sccp_id)

    @extract_id
    def add_endpoint_custom(self, endpoint_custom_id):
        return self.line_endpoint_custom.associate(self.line_id, endpoint_custom_id)

    @extract_id
    def remove_endpoint_custom(self, endpoint_custom_id):
        return self.line_endpoint_custom.dissociate(self.line_id, endpoint_custom_id)

    @extract_id
    def add_device(self, device_id):
        return self.line_device.associate(self.line_id, device_id)

    @extract_id
    def remove_device(self, device_id):
        return self.line_device.dissociate(self.line_id, device_id)

    def get_device(self):
        return self.line_device.get_by_line(self.line_id)

    @extract_id
    def add_application(self, application_uuid):
        return self.line_application.associate(self.line_id, application_uuid)

    @extract_id
    def remove_application(self, application_uuid):
        return self.line_application.dissociate(self.line_id, application_uuid)


class LinesCommand(MultiTenantCommand):

    resource = 'lines'
    relation_cmd = LineRelation
