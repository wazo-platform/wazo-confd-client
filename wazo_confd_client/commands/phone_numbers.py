# Copyright 2024 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import requests

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.util import url_join


class PhoneNumbersCommand(MultiTenantCommand):
    resource = 'phone-numbers'

    def set_main(self, body):
        url = url_join(self.resource, 'main')
        response = self.session.put(url, json=body)
        if response.status_code != requests.codes.ok:
            self.raise_from_response(response)
