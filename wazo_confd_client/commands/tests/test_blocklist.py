# Copyright 2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from unittest import TestCase
from uuid import uuid4

from hamcrest import assert_that, equal_to
from wazo_lib_rest_client.client import PLUGINS_CACHE

from wazo_confd_client.client import ConfdClient
from wazo_confd_client.tests import TestCommand

from ..blocklist import UserBlocklistsCommand


class TestExtensionUserBlocklist(TestCase):
    def setUp(self) -> None:
        self.client = ConfdClient('http://localhost/1.1')

    def test_command_loaded(self):
        print(PLUGINS_CACHE)
        assert hasattr(self.client, 'user_blocklists')
        assert isinstance(self.client.user_blocklists, UserBlocklistsCommand)


class TestUserBlocklists(TestCommand):
    Command = UserBlocklistsCommand

    def test_list_numbers(self):
        user_uuid = str(uuid4())
        response = {
            'total': 1,
            'items': [
                {
                    'uuid': 'test',
                    'label': 'test',
                    'number': '123456789',
                    'user_uuid': user_uuid,
                    'tenant_uuid': 'test',
                }
            ],
        }
        self.set_response('get', 200, response)

        result = self.command.list_numbers(
            label='test',
            number='123456789',
            user_uuid=user_uuid,
        )

        self.session.get.assert_called_once_with(
            '/users/blocklist/numbers',
            params={
                'label': 'test',
                'number': '123456789',
                'user_uuid': user_uuid,
            },
            headers=self.Command.headers,
        )
        assert_that(result, equal_to(response))

    def test_get_number(self):
        response = {
            'uuid': 'test',
            'label': 'test',
            'number': '123456789',
            'user_uuid': 'test',
            'tenant_uuid': 'test',
        }
        self.set_response('get', 200, response)

        result = self.command.get_number('test')

        self.session.get.assert_called_once_with(
            '/users/blocklist/numbers/test', headers=self.Command.headers
        )
        assert_that(result, equal_to(response))
