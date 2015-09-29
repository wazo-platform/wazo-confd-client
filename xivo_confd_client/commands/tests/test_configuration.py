# -*- coding: utf-8 -*-

# Copyright (C) 2014-2015 Avencall
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

from hamcrest import assert_that
from hamcrest import has_entry
from xivo_confd_client.tests import TestCommand

from ..configuration import ConfigurationCommand


class TestInfos(TestCommand):

    Command = ConfigurationCommand

    def test_get(self):
        self.set_response('get', 200, {'enabled': True})

        result = self.command.live_reload.get()

        self.session.get.assert_called_once_with('/configuration/live_reload')
        assert_that(result, has_entry('enabled', True))

    def test_calling_infos_with_no_method(self):
        self.set_response('put', 204)

        self.command.live_reload.put(True)

        self.session.put.assert_called_once_with('/configuration/live_reload', {'enabled': True})
