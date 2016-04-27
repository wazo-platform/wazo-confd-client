# -*- coding: UTF-8 -*-

# Copyright (C) 2016 Avencall
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

from ..wizard import WizardCommand

from xivo_confd_client.tests import TestCommand


class TestWizard(TestCommand):

    Command = WizardCommand

    def test_create(self):
        body = {'admin_password': 'password',
                'etc': '...'}

        expected_content = {'xivo_uuid': 'UUID'}
        expected_url = "/wizard"

        self.set_response('post', 204, expected_content)

        self.command.create(body)

        self.session.post.assert_called_once_with(expected_url, body)

    def test_get(self):
        expected_content = {'configured': False}
        expected_url = "/wizard"
        self.set_response('get', 200, expected_content)

        self.command.get()

        self.session.get.assert_called_once_with(expected_url)

    def test_discover(self):
        expected_url = "/wizard/discover"
        expected_content = {'hostname': 'xivo',
                            'etc': '...'}

        self.set_response('get', 200, expected_content)

        self.command.discover()

        self.session.get.assert_called_once_with(expected_url)
