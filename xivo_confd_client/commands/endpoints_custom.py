# -*- coding: utf-8 -*-
# Copyright (C) 2016 Avencall
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import (LineEndpointCustomRelation,
                                         TrunkEndpointCustomRelation)


class EndpointCustomRelation(object):

    def __init__(self, builder, custom_id):
        self.custom_id = custom_id
        self.line_endpoint_custom = LineEndpointCustomRelation(builder)
        self.trunk_endpoint_custom = TrunkEndpointCustomRelation(builder)

    def associate_line(self, line_id):
        self.line_endpoint_custom.associate(line_id, self.custom_id)

    def dissociate_line(self, line_id):
        self.line_endpoint_custom.dissociate(line_id, self.custom_id)

    def get_line(self):
        return self.line_endpoint_custom.get_by_endpoint_custom(self.custom_id)

    def get_trunk(self):
        return self.trunk_endpoint_custom.get_by_endpoint_custom(self.custom_id)


class EndpointsCustomCommand(CRUDCommand):

    resource = 'endpoints/custom'
    relation_cmd = EndpointCustomRelation
