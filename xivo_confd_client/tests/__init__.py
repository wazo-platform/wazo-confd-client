# -*- coding: utf-8 -*-
# Copyright (C) 2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

import unittest
from mock import Mock

from ..session import ConfdSession


class TestCommand(unittest.TestCase):

    def setUp(self):
        self.session = Mock(ConfdSession)
        self.client = Mock()
        self.client.session.return_value = self.session
        self.command = self.Command(self.client)

    def set_response(self, action, status_code, json=None, content=None):
        response = Mock()
        response.status_code = status_code
        response.json.return_value = json
        response.content = content

        mock_action = getattr(self.session, action)
        mock_action.return_value = response

        return json
