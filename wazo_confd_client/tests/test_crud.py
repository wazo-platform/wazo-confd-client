# Copyright 2014-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that, equal_to

from wazo_confd_client.tests import TestCommand

from ..crud import CRUDCommand


class CRUDCommandTest(CRUDCommand):
    resource = 'test'


class TestCRUD(TestCommand):
    Command = CRUDCommandTest

    def test_list(self):
        expected_response = self.set_response(
            'get',
            200,
            {
                "total": 2,
                "items": [
                    {"id": 1, "firstname": "John"},
                    {"id": 2, "firstname": "Mary"},
                ],
            },
        )

        result = self.command.list(search='term')

        assert_that(result, equal_to(expected_response))
        self.session.get.assert_called_once_with('/test', params={'search': 'term'})

    def test_get(self):
        resource_id = 1
        expected_url = f"/test/{resource_id}"
        expected_response = self.set_response(
            'get', 200, {'id': resource_id, 'firstname': 'John'}
        )

        result = self.command.get(resource_id)

        assert_that(result, equal_to(expected_response))
        self.session.get.assert_called_once_with(expected_url)

    def test_create(self):
        expected_url = "/test"
        expected_response = self.set_response(
            'post', 201, {'id': 1, 'firstname': 'John'}
        )

        body = {'firstname': 'John'}

        result = self.command.create(body)

        assert_that(result, equal_to(expected_response))
        self.session.post.assert_called_once_with(expected_url, body)

    def test_update(self):
        resource_id = 1
        expected_url = f"/test/{resource_id}"
        self.set_response('put', 204)

        body = {
            'id': resource_id,
            'firstname': 'John',
            'links': [{'rel': 'users', 'href': 'http://localhost/users/1'}],
        }

        expected_body = {'id': resource_id, 'firstname': 'John'}

        self.command.update(body)

        self.session.put.assert_called_once_with(expected_url, expected_body)

    def test_update_with_uuid(self):
        resource_uuid = 'abcd-123'
        expected_url = f"/test/{resource_uuid}"
        self.set_response('put', 204)

        body = {
            'uuid': resource_uuid,
            'firstname': 'John',
            'links': [{'rel': 'users', 'href': 'http://localhost/users/1'}],
        }

        expected_body = {'uuid': resource_uuid, 'firstname': 'John'}

        self.command.update(body)

        self.session.put.assert_called_once_with(expected_url, expected_body)

    def test_update_with_no_uuid_or_id(self):
        body = {'firstname': 'John'}
        self.assertRaises(KeyError, self.command.update, body)

    def test_delete(self):
        resource_id = 1
        expected_url = f"/test/{resource_id}"
        self.set_response('delete', 204)

        self.command.delete(resource_id)

        self.session.delete.assert_called_once_with(expected_url)
