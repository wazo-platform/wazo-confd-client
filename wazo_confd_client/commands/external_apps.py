# Copyright 2020-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.util import url_join, extract_name
from wazo_confd_client.crud import MultiTenantCommand


class ExternalAppsCommand(MultiTenantCommand):

    resource = 'external/apps'

    @extract_name()
    def get(self, resource_id):
        url = url_join(self.resource, resource_id)
        response = self.session.get(url)
        return response.json()

    @extract_name(pass_original=True)
    def create(self, name, body):
        url = url_join(self.resource, name)
        response = self.session.post(url, body)
        return response.json()

    @extract_name(pass_original=True)
    def update(self, name, body):
        url = url_join(self.resource, name)
        body = {key: value for key, value in body.items() if key != "links"}
        self.session.put(url, body)

    @extract_name()
    def delete(self, resource_id):
        url = url_join(self.resource, resource_id)
        self.session.delete(url)
