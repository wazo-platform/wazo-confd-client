# Copyright 2015-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from unittest import TestCase
from unittest.mock import ANY, Mock
from uuid import uuid4

from hamcrest import assert_that, equal_to

from wazo_confd_client.tests import TestCommand

from ..users import UserRelation, UsersCommand

FAKE_UUID = '00000000-aaaa-1111-bbbb-222222222222'


class TestUsers(TestCommand):
    Command = UsersCommand

    def test_import_csv(self):
        csvdata = "firstname\nToto\n"
        expected_content = {'created': [{'user_id': 1}]}
        expected_url = "/users/import"
        expected_headers = {
            'Content-Type': 'text/csv; charset=utf-8',
            'Wazo-Tenant': ANY,
        }

        self.set_response('post', 204, expected_content)

        self.command.import_csv(csvdata)

        self.session.post.assert_called_once_with(
            expected_url,
            raw=csvdata,
            check_response=False,
            timeout=300,
            headers=expected_headers,
        )

    def test_update_csv(self):
        csvdata = "firstname\nToto\n"
        expected_content = {'updated': [{'user_id': 1}]}
        expected_url = "/users/import"
        expected_headers = {'Content-Type': 'text/csv; charset=utf-8'}

        self.set_response('put', 204, expected_content)

        self.command.update_csv(csvdata)

        self.session.put.assert_called_once_with(
            expected_url,
            raw=csvdata,
            check_response=False,
            timeout=300,
            headers=expected_headers,
        )

    def test_export_csv(self):
        expected_url = "/users/export"
        expected_content = "firstname\nToto\n"

        self.set_response('get', 200, content=expected_content)

        result = self.command.export_csv()

        assert_that(result, equal_to(expected_content))
        self.session.get.assert_called_once_with(
            expected_url,
            headers={'Accept': 'text/csv; charset=utf-8', 'Wazo-Tenant': ANY},
        )

    def test_main_endpoint_sip(self):
        expected_url = f"/users/{FAKE_UUID}/lines/main/associated/endpoints/sip"
        expected_content = {"username": 'tata'}

        self.set_response('get', 200, json=expected_content)

        result = self.command.get_main_endpoint_sip(FAKE_UUID)

        assert_that(result, equal_to(expected_content))
        self.session.get.assert_called_once_with(expected_url, params={})

    def test_list_user_me_blocklist_numbers(self):
        response = {
            'total': 10,
            'items': [
                {
                    'uuid': (number_uuid := str(uuid4())),
                    'label': f'test {i}',
                    'number': f'123456789{i}',
                    'links': {
                        'users_me_blocklist_number': f'/users/me/blocklist/numbers/{number_uuid}'
                    },
                }
                for i in range(10)
            ],
        }
        self.set_response('get', 200, json=response)

        result = self.command.my_blocklist.numbers.list(
            label='test',
            number='123456789',
        )

        assert_that(result, equal_to(response))
        self.session.get.assert_called_once_with(
            '/users/me/blocklist/numbers',
            params={
                'label': 'test',
                'number': '123456789',
            },
        )

    def test_get_users_me_blocklist_number(self):
        response = {
            'uuid': (number_uuid := str(uuid4())),
            'label': 'test',
            'number': '1234567890',
            'links': {
                'users_me_blocklist_number': f'/users/me/blocklist/numbers/{number_uuid}'
            },
        }
        self.set_response('get', 200, json=response)

        result = self.command.my_blocklist.numbers(number_uuid).get()

        assert_that(result, equal_to(response))
        self.session.get.assert_called_once_with(
            f'/users/me/blocklist/numbers/{number_uuid}'
        )

    def test_create_users_me_blocklist_number(self):
        number = {
            'label': 'test',
            'number': '1234567890',
        }
        response = {
            'uuid': (number_uuid := str(uuid4())),
            **number,
            'links': {
                'users_me_blocklist_number': f'/users/me/blocklist/numbers/{number_uuid}'
            },
        }
        self.set_response('post', 201, json=response)

        result = self.command.my_blocklist.numbers.create(number)

        assert_that(result, equal_to(response))
        self.session.post.assert_called_once_with(
            '/users/me/blocklist/numbers', json=number
        )

    def test_update_users_me_blocklist_number(self):
        number = {
            'label': 'test',
            'number': '1234567890',
        }
        number_uuid = str(uuid4())

        self.set_response('put', 204)

        result = self.command.my_blocklist.numbers(number_uuid).update(number)

        assert_that(result, equal_to(None))
        self.session.put.assert_called_once_with(
            f'/users/me/blocklist/numbers/{number_uuid}', json=number
        )

    def test_delete_users_me_blocklist_number(self):
        number_uuid = str(uuid4())
        self.set_response('delete', 204)

        result = self.command.my_blocklist.numbers(number_uuid).delete()

        assert_that(result, equal_to(None))
        self.session.delete.assert_called_once_with(
            f'/users/me/blocklist/numbers/{number_uuid}'
        )

    def test_lookup_user_blocklist_numbers(self):
        blocklist_number_uuid = str(uuid4())
        self.set_response(
            'head', 200, headers={'Wazo-Blocklist-Number-UUID': blocklist_number_uuid}
        )

        result = self.command(FAKE_UUID).blocklist.numbers.lookup(
            number_exact='1234567890'
        )

        assert_that(result, equal_to(blocklist_number_uuid))
        self.session.head.assert_called_once_with(
            f'/users/{FAKE_UUID}/blocklist/numbers',
            params={'number_exact': '1234567890'},
            check_response=False,
        )

    def test_lookup_user_blocklist_numbers_not_found(self):
        self.set_response('head', 404)

        result = self.command(FAKE_UUID).blocklist.numbers.lookup(
            number_exact='1234567890'
        )

        assert_that(result, equal_to(None))
        self.session.head.assert_called_once_with(
            f'/users/{FAKE_UUID}/blocklist/numbers',
            params={'number_exact': '1234567890'},
            check_response=False,
        )


class TestUserRelation(TestCase):
    def test_get_funckey(self):
        user_id = 34
        position = 1

        relation = UserRelation(Mock(), user_id)
        relation.user_funckey = Mock()

        relation.get_funckey(position)

        relation.user_funckey.get_funckey.assert_called_once_with(user_id, position)
