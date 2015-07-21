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

import abc

from xivo_lib_rest_client import HTTPCommand
from xivo_confd_client.util import extract_id, url_join


class CRUDCommand(HTTPCommand):

    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def resource(self):
        return

    @property
    def relation_cmd(self):
        raise NotImplementedError("Command needs to implement an Associatior")

    def list(self, **kwargs):
        url = url_join(self.resource)
        response = self.session.get(url, params=kwargs)
        return response.json()

    @extract_id
    def get(self, resource_id):
        url = url_join(self.resource, resource_id)
        response = self.session.get(url)
        return response.json()

    def create(self, body):
        url = url_join(self.resource)
        response = self.session.post(url, body)
        return response.json()

    def update(self, body):
        url = url_join(self.resource, body['id'])
        body = {key: value for key, value in body.iteritems() if key != "links"}
        self.session.put(url, body)

    @extract_id
    def delete(self, resource_id):
        url = url_join(self.resource, resource_id)
        self.session.delete(url)

    @extract_id
    def relations(self, resource_id):
        return self.relation_cmd(self._session_builder, resource_id)

    def __call__(self, resource):
        return self.relations(resource)
