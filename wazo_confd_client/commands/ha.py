# Copyright 2019-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import HTTPCommand
from wazo_confd_client.util import url_join


class HACommand(HTTPCommand):

    headers = {'Accept': 'application/json'}

    def get(self):
        url = url_join('ha')
        r = self.session.get(url, headers=self.headers)

        return r.json()

    def update(self, body):
        url = url_join('ha')
        self.session.put(url, json=body, headers=self.headers)
