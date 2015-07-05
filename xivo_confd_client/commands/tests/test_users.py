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

from ..users import UsersCommand
from hamcrest import assert_that
from hamcrest import equal_to
from xivo_lib_rest_client.tests.command import HTTPCommandTestCase


class TestUsers(HTTPCommandTestCase):

    Command = UsersCommand

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
        self.session.get.return_value = self.new_response(200, json=expected_content)

        result = self.command.list()

        self.session.get.assert_called_once_with(self.base_url,
                                                 params={},
                                                 headers={'Accept': 'application/json'})
        assert_that(result, equal_to(expected_content))

    def test_list_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.list)

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
        self.session.get.return_value = self.new_response(200, json=expected_content)

        result = self.command.list(view='directory')

        self.session.get.assert_called_once_with(self.base_url,
                                                 params={'view': 'directory'},
                                                 headers={'Accept': 'application/json'})
        assert_that(result, equal_to(expected_content))


    def test_list_funckeys(self):
        pass

    def test_list_funckeys_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.list_funckeys, 1)

    def test_delete_funckeys(self):
        pass

    def test_delete_funckeys_when_not_204(self):
        self.session.delete.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.delete_funckeys, 1)

    def test_get_funckey(self):
        pass

    def test_get_funckey_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.get_funckey, 1, 1)

    def test_delete_funckey(self):
        pass

    def test_delete_funckey_when_not_204(self):
        self.session.delete.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.delete_funckey, 1, 1)

    def test_update_funckey(self):
        pass

    def test_update_funckey_when_not_204(self):
        self.session.put.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.update_funckey, 1, 1, dict())

    def test_dissociate_funckey_template(self):
        pass

    def test_dissociate_funckey_template_when_not_204(self):
        self.session.delete.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.dissociate_funckey_template, 1, 1)

    def test_associate_funckey_template(self):
        pass

    def test_associate_funckey_template_when_not_204(self):
        self.session.put.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.associate_funckey_template, 1, 1, dict())
