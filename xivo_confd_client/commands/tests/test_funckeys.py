# -*- coding: utf-8 -*-

# Copyright (C) 2015 Avencall
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

from ..funckeys import FuncKeysCommand
from hamcrest import assert_that
from hamcrest import equal_to
from hamcrest import none
from xivo_lib_rest_client.tests.command import HTTPCommandTestCase

headers = {'Accept': 'application/json',
           'Content-Type': 'application/json'}

class TestFuncKeys(HTTPCommandTestCase):

    Command = FuncKeysCommand

    def test_list_templates(self):
        expected_content = {'items': [{'id': 2,
                                       'keys': {},
                                       'links': [{'href': 'https://192.168.1.124:9486/1.1/funckeys/templates/2',
                                                  'rel': 'func_key_templates'}],
                                       'name': 'fun'}],
                            'total': 1}

        self.session.get.return_value = self.new_response(200, json=expected_content)

        result = self.command.list_templates()

        expected_url = '{base_url}/templates'.format(base_url=self.base_url)
        self.session.get.assert_called_once_with(expected_url, headers=headers)
        assert_that(result, equal_to(expected_content))

    def test_list_templates_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.list_templates)

    def test_create_template(self):
        self.session.post.return_value = self.new_response(201)

        result = self.command.create_template(dict())

        expected_url = '{base_url}/templates'.format(base_url=self.base_url)
        self.session.post.assert_called_once_with(expected_url, headers=headers, data='{}')
        assert_that(result, none())

    def test_create_template_when_not_201(self):
        data = {'name': 'fun'}
        self.session.post.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.create_template, data)

    def test_get_template(self):
        template_id = 2
        expected_content = {'blf': True,
                            'destination': {'exten': '1234', 'href': None, 'type': 'custom'},
                            'id': 32,
                            'inherited': True,
                            'label': 'pouet',
                            'links': []}

        self.session.get.return_value = self.new_response(200, json=expected_content)

        result = self.command.get_template(template_id)

        expected_url = '{base_url}/templates/{template_id}'.format(base_url=self.base_url, template_id=template_id)
        self.session.get.assert_called_once_with(expected_url, headers=headers)
        assert_that(result, equal_to(expected_content))

    def test_get_template_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.get_template, 2)

    def test_delete_template(self):
        template_id = 2

        self.session.delete.return_value = self.new_response(204)
        result = self.command.delete_template(template_id)

        expected_url = '{base_url}/templates/{template_id}'.format(base_url=self.base_url,
                                                                   template_id=template_id)
        self.session.delete.assert_called_once_with(expected_url, headers=headers)
        assert_that(result, none())

    def test_delete_template_when_not_204(self):
        self.session.delete.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.delete_template, 2)

    def test_get_template_funckey(self):
        template_id = 2
        position = 1
        expected_content = {'blf': True,
                            'destination': {'exten': '1234', 'href': None, 'type': 'custom'},
                            'id': 32,
                            'inherited': True,
                            'label': 'pouet',
                            'links': []}

        self.session.get.return_value = self.new_response(200, json=expected_content)

        result = self.command.get_template_funckey(template_id, position)

        expected_url = '{base_url}/templates/{template_id}/{position}'.format(base_url=self.base_url,
                                                                              template_id=template_id,
                                                                              position=position)
        self.session.get.assert_called_once_with(expected_url, headers=headers)
        assert_that(result, equal_to(expected_content))

    def test_get_template_funckey_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.get_template_funckey, 1, 1)

    def test_delete_template_funckey(self):
        template_id = 2
        position = 1

        self.session.delete.return_value = self.new_response(204)
        result = self.command.delete_template_funckey(template_id, position)

        expected_url = '{base_url}/templates/{template_id}/{position}'.format(base_url=self.base_url,
                                                                              template_id=template_id,
                                                                              position=position)
        self.session.delete.assert_called_once_with(expected_url, headers=headers)
        assert_that(result, none())

    def test_delete_template_funckey_when_not_204(self):
        self.session.delete.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.delete_template_funckey, 1, 1)

    def test_update_template_funckey(self):
        template_id = 2
        position = 1

        self.session.put.return_value = self.new_response(204)
        result = self.command.update_template_funckey(template_id, position, dict())

        expected_url = '{base_url}/templates/{template_id}/{position}'.format(base_url=self.base_url,
                                                                              template_id=template_id,
                                                                              position=position)
        self.session.put.assert_called_once_with(expected_url, headers=headers, data='{}')
        assert_that(result, none())

    def test_update_template_funckey_when_not_204(self):
        self.session.put.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.update_template_funckey, 1, 1, dict())
