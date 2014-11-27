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

from ..users import UsersCommand
from hamcrest import assert_that
from hamcrest import equal_to
from mock import Mock
from requests.exceptions import HTTPError


class TestUsers(unittest.TestCase):

    def setUp(self):
        self.scheme = 'https'
        self.host = 'host'
        self.port = 666
        self.version = '42'
        self.base_url = 'https://host:666/42'
        self.session = Mock()
        self.command = UsersCommand(self.scheme, self.host, self.port, self.version, self.session)

    def test_list(self):
        expected_content = {
            "total": 2,
            "items":
            [
                {
                    "id": 1,
                    "firstname": "John",
                    "lastname": "Doe",
                    "timezone": "",
                    "language": "en_US",
                    "description": "",
                    "caller_id": '"John Doe"',
                    "outgoing_caller_id": "default",
                    "mobile_phone_number": "",
                    "username": "",
                    "password": "",
                    "music_on_hold": "default",
                    "preprocess_subroutine": "",
                    "userfield": ""
                },
                {
                    "id": 2,
                    "firstname": "Mary",
                    "lastname": "Sue",
                    "timezone": "",
                    "language": "fr_FR",
                    "description": "",
                    "caller_id": '"Mary Sue"',
                    "outgoing_caller_id": "default",
                    "mobile_phone_number": "",
                    "username": "",
                    "password": "",
                    "music_on_hold": "default",
                    "preprocess_subroutine": "",
                    "userfield": ""
                }
            ]
        }
        self.session.get.return_value = self._new_response(200, json=expected_content)

        result = self.command.list()

        assert_that(result, equal_to(expected_content))
        self.session.get.assert_called_once_with('{base_url}/users'.format(base_url=self.base_url),
                                                 params={})

    def test_list_when_not_200(self):
        self.session.get.return_value = self._new_response(404)

        self.assertRaises(HTTPError, self.command.list)

    def test_list_with_view(self):
        expected_content = {
            "total": 2,
            "items":
            [
                {
                    "id": 1,
                    "line_id": 1,
                    "agent_id": 1,
                    "firstname": "John",
                    "lastname": "Doe",
                    "exten": "1234",
                    "mobile_phone_number": "+14184765458"
                },
                {
                    "id": 2,
                    "line_id": None,
                    "agent_id": None,
                    "firstname": "Mary",
                    "lastname": "Sue",
                    "exten": "",
                    "mobile_phone_number": ""
                }
            ]
        }
        self.session.get.return_value = self._new_response(200, json=expected_content)

        result = self.command.list(view='directory')

        assert_that(result, equal_to(expected_content))
        self.session.get.assert_called_once_with('{base_url}/users'.format(base_url=self.base_url),
                                                 params={'view': 'directory'})

    @staticmethod
    def _new_response(status_code, json=None):
        response = Mock()
        response.status_code = status_code
        response.raise_for_status.side_effect = HTTPError()
        if json is not None:
            response.json.return_value = json
        return response
