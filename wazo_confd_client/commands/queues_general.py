# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_lib_rest_client import RESTCommand


class QueuesGeneralCommand(RESTCommand):

    resource = 'asterisk/queues/general'

    def get(self):
        response = self.session.get(self.resource)
        return response.json()

    def update(self, body):
        self.session.put(self.resource, body)
