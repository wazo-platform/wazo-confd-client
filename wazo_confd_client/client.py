# -*- coding: utf-8 -*-
# Copyright 2015-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import requests

from wazo_lib_rest_client.client import BaseClient
from wazo_confd_client.session import ConfdSession


class ConfdClient(BaseClient):

    namespace = 'wazo_confd_client.commands'

    def __init__(self,
                 host,
                 port=9486,
                 version='1.1',
                 username=None,
                 password=None,
                 **kwargs):
        super(ConfdClient, self).__init__(
            host=host,
            port=port,
            version=version,
            **kwargs)
        self.username = username
        self.password = password

    def session(self):
        session = super(ConfdClient, self).session()
        if self.username and self.password:
            session.auth = requests.auth.HTTPDigestAuth(self.username, self.password)
        return ConfdSession(session, self.url())
