# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import HTTPCommand


class StatusCommand(HTTPCommand):
    def __call__(self):
        return self.get()

    def get(self):
        r = self.session.get('/status')

        return r.json()
