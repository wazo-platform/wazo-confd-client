# Copyright 2016-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import CRUDCommand
from wazo_confd_client.util import url_join


class EntitiesCommand(CRUDCommand):
    resource = 'entities'

    def create(self, body):
        headers = dict(self.session.WRITE_HEADERS)
        tenant_uuid = body.pop('tenant_uuid', self._client.tenant_uuid)
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = url_join(self.resource)
        response = self.session.post(url, body, headers=headers)
        return response.json()
