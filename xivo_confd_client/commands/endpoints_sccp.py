# -*- coding: UTF-8 -*-

# Copyright (C) 2015 Avencall
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
