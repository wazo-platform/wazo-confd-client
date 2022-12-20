# Copyright 2016-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import HTTPCommand
from wazo_confd_client.util import url_join


class WizardCommand(HTTPCommand):

    resource = 'wizard'

    def create(self, body, timeout=300):
        url = url_join(self.resource)
        response = self.session.post(url, body, timeout=timeout)
        return response.json()

    def get(self):
        url = url_join(self.resource)
        response = self.session.get(url)
        return response.json()

    def discover(self):
        url = url_join(self.resource, "discover")
        response = self.session.get(url)
        return response.json()

    def __call__(self):
        return self.get()
