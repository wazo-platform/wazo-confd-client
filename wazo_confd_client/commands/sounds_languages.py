# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand
from wazo_confd_client.util import url_join


class SoundsLanguagesCommand(RESTCommand):
    resource = 'sounds/languages'

    def list(self):
        url = url_join(self.resource)
        response = self.session.get(url)
        return response.json()
