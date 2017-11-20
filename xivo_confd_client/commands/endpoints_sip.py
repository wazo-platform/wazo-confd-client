# -*- coding: UTF-8 -*-
# Copyright (C) 2015-2016 Avencall
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import (LineEndpointSipRelation,
                                         TrunkEndpointSipRelation)


class EndpointSipRelation(object):

    def __init__(self, builder, sip_id):
        self.sip_id = sip_id
        self.line_endpoint_sip = LineEndpointSipRelation(builder)
        self.trunk_endpoint_sip = TrunkEndpointSipRelation(builder)

    def associate_line(self, line_id):
        self.line_endpoint_sip.associate(line_id, self.sip_id)

    def dissociate_line(self, line_id):
        self.line_endpoint_sip.dissociate(line_id, self.sip_id)

    def get_line(self):
        return self.line_endpoint_sip.get_by_endpoint_sip(self.sip_id)

    def get_trunk(self):
        return self.trunk_endpoint_sip.get_by_endpoint_sip(self.sip_id)


class EndpointsSipCommand(CRUDCommand):

    resource = 'endpoints/sip'
    relation_cmd = EndpointSipRelation
