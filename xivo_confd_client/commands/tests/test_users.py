# -*- coding: utf-8 -*-
# Copyright 2015-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from unittest import TestCase

from hamcrest import assert_that, equal_to
from mock import ANY, Mock

from xivo_confd_client.tests import TestCommand

from ..users import UsersCommand
from ..users import UserRelation

FAKE_UUID = '00000000-aaaa-1111-bbbb-222222222222'


class TestUsers(TestCommand):

    Command = UsersCommand

    def test_import_csv(self):
        csvdata = "firstname\nToto\n"
        expected_content = {'created': [{'user_id': 1}]}
        expected_url = "/users/import"
        expected_headers = {'Content-Type': 'text/csv; charset=utf-8', 'Wazo-Tenant': ANY}

        self.set_response('post', 204, expected_content)

        self.command.import_csv(csvdata)

        self.session.post.assert_called_once_with(expected_url,
                                                  raw=csvdata,
                                                  check_response=False,
                                                  timeout=300,
                                                  headers=expected_headers)

    def test_update_csv(self):
        csvdata = "firstname\nToto\n"
        expected_content = {'updated': [{'user_id': 1}]}
        expected_url = "/users/import"
        expected_headers = {'Content-Type': 'text/csv; charset=utf-8'}

        self.set_response('put', 204, expected_content)

        self.command.update_csv(csvdata)

        self.session.put.assert_called_once_with(expected_url,
                                                 raw=csvdata,
                                                 check_response=False,
                                                 timeout=300,
                                                 headers=expected_headers)

    def test_export_csv(self):
        expected_url = "/users/export"
        expected_content = "firstname\nToto\n"

        self.set_response('get', 200, content=expected_content)

        result = self.command.export_csv()

        assert_that(result, equal_to(expected_content))
        self.session.get.assert_called_once_with(expected_url, headers={'Accept': 'text/csv; charset=utf-8'})

    def test_main_endpoint_sip(self):
        expected_url = "/users/{}/lines/main/associated/endpoints/sip".format(FAKE_UUID)
        expected_content = {"username": 'tata'}

        self.set_response('get', 200, json=expected_content)

        result = self.command.get_main_endpoint_sip(FAKE_UUID)

        assert_that(result, equal_to(expected_content))
        self.session.get.assert_called_once_with(expected_url)


class TestUserRelation(TestCase):

    def test_get_funckey(self):
        user_id = 34
        position = 1

        relation = UserRelation(Mock(), user_id)
        relation.user_funckey = Mock()

        relation.get_funckey(position)

        relation.user_funckey.get_funckey.assert_called_once_with(user_id, position)
