# Copyright 2015-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import LineEndpointSccpRelation


class EndpointSccpRelation:
    def __init__(self, builder, sccp_id):
        self.sccp_id = sccp_id
        self.line_endpoint_sccp = LineEndpointSccpRelation(builder)

    def associate_line(self, line_id):
        self.line_endpoint_sccp.associate(line_id, self.sccp_id)

    def dissociate_line(self, line_id):
        self.line_endpoint_sccp.dissociate(line_id, self.sccp_id)


class EndpointsSccpCommand(MultiTenantCommand):
    resource = 'endpoints/sccp'
    relation_cmd = EndpointSccpRelation
