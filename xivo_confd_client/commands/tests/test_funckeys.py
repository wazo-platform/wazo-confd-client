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
from xivo_lib_rest_client.tests.command import HTTPCommandTestCase


class TestFuncKeys(HTTPCommandTestCase):

    Command = FuncKeysCommand

    def test_list_templates(self):
        expected_content = {u'items': [{u'id': 2,
                                        u'keys': {},
                                        u'links': [{u'href': u'https://192.168.1.124:9486/1.1/funckeys/templates/2',
                                                    u'rel': u'func_key_templates'}],
                                        u'name': u'fun'}],
                            u'total': 1}

        self.session.get.return_value = self.new_response(200, json=expected_content)

        result = self.command.list_templates()

        self.session.get.assert_called_once_with('{base_url}/templates'.format(base_url=self.base_url),
                                                 headers={'Accept': 'application/json',
                                                          'Content-Type': 'application/json'})
        assert_that(result, equal_to(expected_content))

    def test_list_templates_when_not_200(self):
        self.session.get.return_value = self.new_response(404)

        self.assertRaisesHTTPError(self.command.list_templates)
