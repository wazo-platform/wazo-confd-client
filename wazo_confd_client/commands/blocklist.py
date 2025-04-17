# Copyright 2019-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import HTTPCommand

from wazo_confd_client.util import url_join


class UserBlocklistsCommand(HTTPCommand):
    headers = {'Accept': 'application/json'}
    resource = 'users/blocklist/numbers'

    def list_numbers(self, **kwargs):
        url = url_join(self.resource)
        response = self.session.get(url, headers=self.headers, params=kwargs)

        return response.json()

    def get_number(self, number_uuid):
        url = url_join(self.resource, number_uuid)
        response = self.session.get(url, headers=self.headers)

        return response.json()
