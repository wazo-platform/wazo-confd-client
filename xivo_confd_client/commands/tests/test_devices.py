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

from ..devices import DevicesCommand

from xivo_confd_client.tests import TestCommand


class TestFuncKeys(TestCommand):

    Command = DevicesCommand

    def test_autoprov(self):
        device_id = "a1b2c3d4e5f6g7h8i9j0k1l2"
        expected_url = "/devices/{}/autoprov".format(device_id)

        self.set_response('get', 204)

        self.command.autoprov(device_id)

        self.session.get.assert_called_once_with(expected_url)

    def test_synchronize(self):
        device_id = "a1b2c3d4e5f6g7h8i9j0k1l2"
        expected_url = "/devices/{}/synchronize".format(device_id)

        self.set_response('get', 204)

        self.command.synchronize(device_id)

        self.session.get.assert_called_once_with(expected_url)
