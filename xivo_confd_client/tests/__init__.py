# -*- coding: UTF-8 -*-

# Copyright (C) 2015 Avencall
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import unittest
from mock import Mock

from ..session import ConfdSession


class TestCommand(unittest.TestCase):

    def setUp(self):
        self.session = Mock(ConfdSession)
        self.session_builder = Mock()
        self.session_builder.session.return_value = self.session
        self.command = self.Command(self.session_builder)

    def set_response(self, action, status_code, json=None):
        response = Mock()
        response.status_code = status_code
        response.json.return_value = json

        mock_action = getattr(self.session, action)
        mock_action.return_value = response

        return json
