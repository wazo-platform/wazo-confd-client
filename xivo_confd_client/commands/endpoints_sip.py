# -*- coding: UTF-8 -*-

# Copyright (C) 2015-2016 Avencall
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


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
