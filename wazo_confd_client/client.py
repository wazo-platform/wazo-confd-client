# -*- coding: utf-8 -*-
# Copyright 2015-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.client import BaseClient
from wazo_confd_client.session import ConfdSession


class ConfdClient(BaseClient):

    namespace = 'wazo_confd_client.commands'

    def __init__(self, host, port=443, prefix='/api/confd', version='1.1', **kwargs):
        super(ConfdClient, self).__init__(
            host=host, port=port, prefix=prefix, version=version, **kwargs
        )

    def session(self):
        session = super(ConfdClient, self).session()
        return ConfdSession(session, self.url())
