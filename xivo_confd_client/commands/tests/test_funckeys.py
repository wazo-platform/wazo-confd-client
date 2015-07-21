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

from xivo_confd_client.tests import TestCommand


class TestFuncKeys(TestCommand):

    Command = FuncKeysCommand

    def test_get_template_funckey(self):
        template_id = 2
        position = 1
        expected_url = "/funckeys/templates/{}/{}".format(template_id, position)
        expected_content = {'blf': True,
                            'destination': {'exten': '1234', 'href': None, 'type': 'custom'},
                            'id': 32,
                            'inherited': True,
                            'label': 'pouet',
                            'links': []}

        self.set_response('get', 200, expected_content)

        result = self.command.get_template_funckey(template_id, position)

        self.session.get.assert_called_once_with(expected_url)
        assert_that(result, equal_to(expected_content))

    def test_delete_template_funckey(self):
        template_id = 2
        position = 1
        expected_url = "/funckeys/templates/{}/{}".format(template_id, position)

        self.set_response('delete', 204)

        result = self.command.delete_template_funckey(template_id, position)

        self.session.delete.assert_called_once_with(expected_url)
        assert_that(result, none())

    def test_update_template_funckey(self):
        template_id = 2
        position = 1
        expected_url = "/funckeys/templates/{}/{}".format(template_id, position)
        funckey = {'blf': False}

        self.set_response('put', 204)

        result = self.command.update_template_funckey(template_id, position, funckey)

        self.session.put.assert_called_once_with(expected_url, funckey)
        assert_that(result, none())
