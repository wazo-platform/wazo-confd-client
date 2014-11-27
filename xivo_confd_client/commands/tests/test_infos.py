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
from hamcrest import assert_that
from hamcrest import equal_to
from mock import Mock
from requests.exceptions import HTTPError


class TestInfos(unittest.TestCase):

    def setUp(self):
        self.scheme = 'https'
        self.host = 'example.com'
        self.port = 9486
        self.version = '1.1'
        self.base_url = 'https://example.com:9486/1.1'
        self.session = Mock()
        self.command = InfosCommand(self.scheme, self.host, self.port, self.version, self.session)

    def test_get(self):
        self.session.get.return_value = self._new_response(200, json={'uuid': 'test'})

        result = self.command.get()

        self.session.get.assert_called_once_with('{base_url}/infos'.format(base_url=self.base_url))
        assert_that(result, equal_to({'uuid': 'test'}))

    def test_calling_infos_with_no_method(self):
        self.session.get.return_value = self._new_response(200, json={'uuid': 'test'})

        result = self.command()

        self.session.get.assert_called_once_with('{base_url}/infos'.format(base_url=self.base_url))
        assert_that(result, equal_to({'uuid': 'test'}))

    def test_when_not_200(self):
        self.session.get.return_value = self._new_response(404)

        self.assertRaises(HTTPError, self.command)

    @staticmethod
    def _new_response(status_code, json=None):
        response = Mock()
        response.status_code = status_code
        response.raise_for_status.side_effect = HTTPError()
        if json is not None:
            response.json.return_value = json
        return response
