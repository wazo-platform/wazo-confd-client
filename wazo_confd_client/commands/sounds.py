# -*- coding: utf-8 -*-
# Copyright 2017-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from six.moves.urllib.parse import quote

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.util import extract_id, url_join


class SoundsCommand(MultiTenantCommand):

    resource = 'sounds'

    def get(self, category, tenant_uuid=None):
        tenant_uuid = tenant_uuid or self._client.tenant_uuid
        headers = dict(self.session.READ_HEADERS)
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = url_join(self.resource, category)
        response = self.session.get(url, headers=headers)
        return response.json()

    def delete(self, category, tenant_uuid=None):
        tenant_uuid = tenant_uuid or self._client.tenant_uuid
        headers = dict(self.session.READ_HEADERS)
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = url_join(self.resource, category)
        self.session.delete(url, headers=headers)

    @extract_id
    def download_file(self, category, filename, **kwargs):
        tenant_uuid = kwargs.pop('tenant_uuid', None) or self._client.tenant_uuid
        headers = {'Accept': '*/*'}
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = url_join(self.resource, category, 'files', quote(filename, safe=''))
        response = self.session.get(url, headers=headers, params=kwargs)
        return response

    @extract_id
    def upload_file(self, category, filename, content, **kwargs):
        tenant_uuid = kwargs.pop('tenant_uuid', None) or self._client.tenant_uuid
        headers = {'Content-Type': 'application/octet-stream'}
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = url_join(self.resource, category, 'files', filename)
        self.session.put(url, raw=content, headers=headers, params=kwargs)

    @extract_id
    def delete_file(self, category, filename, **kwargs):
        tenant_uuid = kwargs.pop('tenant_uuid', None) or self._client.tenant_uuid
        headers = {}
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = url_join(self.resource, category, 'files', filename)
        self.session.delete(url, headers=headers, params=kwargs)
