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

from ..infos import InfosCommand
from hamcrest import assert_that
from hamcrest import equal_to
from xivo_confd_client.tests import TestCommand


class TestInfos(TestCommand):

    Command = InfosCommand

    def test_get(self):
        self.set_response('get', 200, {'uuid': 'test'})

        result = self.command.get()

        self.session.get.assert_called_once_with('/info')
        assert_that(result, equal_to({'uuid': 'test'}))

    def test_calling_infos_with_no_method(self):
        self.set_response('get', 200, {'uuid': 'test'})

        result = self.command()

        self.session.get.assert_called_once_with('/info')
        assert_that(result, equal_to({'uuid': 'test'}))
