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


from ..users import UsersCommand

from xivo_confd_client.tests import TestCommand


class TestUsers(TestCommand):

    Command = UsersCommand

    def test_import_csv(self):
        csvdata = "firstname\nToto\n"
        expected_content = {'created': [{'user_id': 1}]}
        expected_url = "/users/import"
        expected_headers = {'Content-Type': 'text/csv; charset=utf-8'}

        self.set_response('post', 204, expected_content)

        self.command.import_csv(csvdata)

        self.session.post.assert_called_once_with(expected_url,
                                                  raw=csvdata,
                                                  check_response=False,
                                                  timeout=300,
                                                  headers=expected_headers)