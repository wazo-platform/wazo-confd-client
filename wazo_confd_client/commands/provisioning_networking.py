# Copyright 2019-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import HTTPCommand
from wazo_confd_client.util import url_join


class ProvisioningNetworkingCommand(HTTPCommand):

    headers = {'Accept': 'application/json'}

    def get(self):
        url = url_join('provisioning', 'networking')
        r = self.session.get(url, headers=self.headers)

        return r.json()

    def update(self, body):
        url = url_join('provisioning', 'networking')
        self.session.put(url, json=body, headers=self.headers)
