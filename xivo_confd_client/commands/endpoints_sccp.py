# -*- coding: UTF-8 -*-
# Copyright (C) 2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import LineEndpointSccpRelation


class EndpointSccpRelation(object):

    def __init__(self, builder, sccp_id):
        self.sccp_id = sccp_id
        self.line_endpoint_sccp = LineEndpointSccpRelation(builder)

    def associate_line(self, line_id):
        self.line_endpoint_sccp.associate(line_id, self.sccp_id)

    def dissociate_line(self, line_id):
        self.line_endpoint_sccp.dissociate(line_id, self.sccp_id)

    def get_line(self):
        return self.line_endpoint_sccp.get_by_endpoint_sccp(self.sccp_id)


class EndpointsSccpCommand(CRUDCommand):

    resource = 'endpoints/sccp'
    relation_cmd = EndpointSccpRelation
