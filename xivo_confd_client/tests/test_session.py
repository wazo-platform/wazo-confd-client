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
import json

from mock import Mock
from hamcrest import assert_that, equal_to

from requests import Session
from xivo_confd_client.session import ConfdSession


class TestConfdSession(unittest.TestCase):

    def setUp(self):
        self.session = Mock(Session)
        self.base_url = "http://localhost/1.1"
        self.confd_session = ConfdSession(self.session, self.base_url)

    def set_response(self, action, status_code):
        response = Mock()
        response.status_code = status_code

        mock_action = getattr(self.session, action)
        mock_action.return_value = response
        return response

    def test_get(self):
        expected_url = "{}/users".format(self.base_url)
        expected_response = self.set_response('get', 200)

        result = self.confd_session.get("/users", params={'search': 'term'})

        assert_that(result, equal_to(expected_response))
        self.session.get.assert_called_once_with(expected_url,
                                                 params={'search': 'term'},
                                                 headers={'Accept': 'application/json'})

    def test_post(self):
        expected_url = "{}/users".format(self.base_url)
        expected_response = self.set_response('post', 201)

        body = {'firstname': 'John'}

        result = self.confd_session.post("/users", body)

        assert_that(result, equal_to(expected_response))
        self.session.post.assert_called_once_with(expected_url,
                                                  data=json.dumps(body),
                                                  headers={'Accept': 'application/json',
                                                           'Content-Type': 'application/json'})

    def test_put(self):
        expected_url = "{}/users/1".format(self.base_url)
        self.set_response('put', 204)

        body = {'id': 1,
                'firstname': 'John'}

        self.confd_session.put("/users/1", body)

        self.session.put.assert_called_once_with(expected_url,
                                                 data=json.dumps(body),
                                                 headers={'Accept': 'application/json',
                                                          'Content-Type': 'application/json'})

    def test_delete(self):
        expected_url = "{}/users/1".format(self.base_url)
        self.set_response('delete', 204)

        self.confd_session.delete("/users/1")

        self.session.delete.assert_called_once_with(expected_url, headers={'Accept': 'application/json'})

    def test_given_status_ok_then_no_error_raised(self):
        response = Mock()

        response.status_code = 200
        self.confd_session.check_response(response)

        response.status_code = 201
        self.confd_session.check_response(response)

        response.status_code = 204
        self.confd_session.check_response(response)

        call_count = response.raise_for_status.call_count
        assert_that(call_count, equal_to(0))

    def test_given_status_not_ok_then_error_raised(self):
        response = Mock()
        response.status_code = 400
        response.json.return_value = ["error message"]

        self.confd_session.check_response(response)

        response.raise_for_status.assert_called_once_with()
        assert_that(response.reason, equal_to("error message"))

    def test_clean_url_strips_extra_slashes(self):
        self.confd_session.base_url = "http://localhost//"
        part = "///users/1"

        url = self.confd_session.clean_url(part)

        assert_that(url, equal_to('http://localhost/users/1'))
