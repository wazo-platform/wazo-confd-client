# -*- coding: utf-8 -*-
# Copyright 2016-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.util import url_join
from xivo_confd_client.crud import CRUDCommand


class EntitiesCommand(CRUDCommand):

    resource = 'entities'

    def create(self, body):
        headers = self.session.WRITE_HEADERS
        tenant_uuid = body.pop('tenant_uuid', self._client.tenant())
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = url_join(self.resource)
        response = self.session.post(url, body, headers=headers)
        return response.json()
