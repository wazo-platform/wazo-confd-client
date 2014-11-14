# -*- coding: utf-8 -*-

# Copyright (C) 2014 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import unittest

from ..infos import InfosCommand
from ..exceptions import UnexpectedResultError
from hamcrest import assert_that
from hamcrest import equal_to
from mock import Mock


class TestInfos(unittest.TestCase):

    def setUp(self):
        self.host = 'example.com'
        self.port = 9487
        self.version = '1.1'
        self.base_url = 'https://example.com:9487/1.1'

    def _make_cmd(self):
        return InfosCommand(self.host, self.port, self.version, True)

    def test_get(self):
        session = Mock()
        session.get.return_value = Mock(content='''{"uuid": "test"}''',
                                        status_code=200)

        cmd = self._make_cmd()
        result = cmd.get(session)

        session.get.assert_called_once_with('{base_url}/infos'.format(base_url=self.base_url))
        assert_that(result, equal_to({'uuid': 'test'}))

    def test_calling_infos_with_no_method(self):
        session = Mock()
        session.get.return_value = Mock(content='''{"uuid": "test"}''',
                                        status_code=200)

        cmd = self._make_cmd()
        result = cmd(session)

        session.get.assert_called_once_with('{base_url}/infos'.format(base_url=self.base_url))
        assert_that(result, equal_to({'uuid': 'test'}))

    def test_when_not_200(self):
        session = Mock()
        session.get.return_value = Mock(status_code=404)

        cmd = self._make_cmd()

        self.assertRaises(UnexpectedResultError, cmd, session)
