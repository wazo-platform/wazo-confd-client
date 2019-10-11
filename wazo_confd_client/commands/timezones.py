# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand
from wazo_confd_client.util import url_join


class TimezonesCommand(RESTCommand):

    resource = 'timezones'

    def list(self):
        url = url_join(self.resource)
        response = self.session.get(url)
        return response.json()
