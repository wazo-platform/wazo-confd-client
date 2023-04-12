# Copyright 2020-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand


class PJSIPDocCommand(RESTCommand):
    resource = 'asterisk/pjsip/doc'

    def get(self):
        response = self.session.get(self.resource)
        return response.json()
