# -*- coding: utf-8 -*-
# Copyright 2015-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import (
    LineEndpointSipRelation,
    TrunkEndpointSipRelation,
)


class EndpointSipRelation(object):
    def __init__(self, builder, sip_id):
        self.sip_id = sip_id
        self.line_endpoint_sip = LineEndpointSipRelation(builder)
        self.trunk_endpoint_sip = TrunkEndpointSipRelation(builder)

    def associate_line(self, line_id):
        self.line_endpoint_sip.associate(line_id, self.sip_id)

    def dissociate_line(self, line_id):
        self.line_endpoint_sip.dissociate(line_id, self.sip_id)


class EndpointsSipCommand(MultiTenantCommand):

    resource = 'endpoints/sip'
    relation_cmd = EndpointSipRelation
