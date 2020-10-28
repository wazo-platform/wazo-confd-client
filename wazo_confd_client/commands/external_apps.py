# -*- coding: utf-8 -*-
# Copyright 2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import six

from functools import wraps

from wazo_confd_client.util import url_join
from wazo_confd_client.crud import MultiTenantCommand


def extract_name(func):
    @wraps(func)
    def wrapper(self, resource_or_id, *args, **kwargs):
        if isinstance(resource_or_id, dict):
            if 'name' in resource_or_id:
                resource_id = resource_or_id['name']
            else:
                raise KeyError('no "name" key found')
        else:
            resource_id = resource_or_id
        return func(self, resource_id, *args, **kwargs)

    return wrapper


class ExternalAppsCommand(MultiTenantCommand):

    resource = 'external/apps'

    @extract_name
    def get(self, resource_id):
        url = url_join(self.resource, resource_id)
        response = self.session.get(url)
        return response.json()

    def create(self, body):
        resource_id = body.pop('name', None)
        url = url_join(self.resource, resource_id)
        response = self.session.post(url, body)
        return response.json()

    def update(self, body):
        resource_id = body.get('name')
        url = url_join(self.resource, resource_id)
        body = {key: value for key, value in six.iteritems(body) if key != "links"}
        self.session.put(url, body)

    @extract_name
    def delete(self, resource_id):
        url = url_join(self.resource, resource_id)
        self.session.delete(url)
