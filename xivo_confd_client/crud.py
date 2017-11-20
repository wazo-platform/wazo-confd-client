# -*- coding: UTF-8 -*-
# Copyright 2015-2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import abc
import six

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
        resource_id = body.get('uuid')
        if not resource_id:
            resource_id = body['id']
        url = url_join(self.resource, resource_id)
        body = {key: value for key, value in six.iteritems(body) if key != "links"}
        self.session.put(url, body)

    @extract_id
    def delete(self, resource_id):
        url = url_join(self.resource, resource_id)
        self.session.delete(url)

    @extract_id
    def relations(self, resource_id):
        return self.relation_cmd(self._client, resource_id)

    def __call__(self, resource):
        return self.relations(resource)
