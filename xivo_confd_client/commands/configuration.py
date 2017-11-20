# -*- coding: utf-8 -*-
# Copyright (C) 2014-2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import HTTPCommand
from xivo_confd_client.util import url_join


class LiveReloadCommand(HTTPCommand):

    def get(self):
        url = url_join('configuration', 'live_reload')
        r = self.session.get(url)

        return r.json()

    def update(self, body):
        url = url_join('configuration', 'live_reload')
        self.session.put(url, body)


class ConfigurationCommand(object):

    def __init__(self, client):
        self.live_reload = LiveReloadCommand(client)
