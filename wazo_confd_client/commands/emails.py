# Copyright 2021-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand


class EmailsCommand(RESTCommand):
    resource = 'emails'

    def get(self):
        r = self.session.get(self.resource)
        return r.json()

    def update(self, body):
        self.session.put(self.resource, body)
