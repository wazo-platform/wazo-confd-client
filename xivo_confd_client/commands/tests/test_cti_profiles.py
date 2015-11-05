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
from hamcrest import has_entries
from xivo_confd_client.tests import TestCommand

from ..cti_profiles import CtiProfilesCommand


class TestCtiProfilesCommand(TestCommand):

    Command = CtiProfilesCommand

    def test_list(self):
        self.set_response('get', 200, {'total': 0,
                                       'items': []})

        result = self.command.list()

        self.session.get.assert_called_once_with('/cti_profiles')
        assert_that(result, has_entries(total=0,
                                        items=[]))

    def test_get(self):
        cti_profile_id = 1
        self.set_response('get', 200, {'id': cti_profile_id,
                                       'name': 'client'})

        result = self.command.get(cti_profile_id)

        self.session.get.assert_called_once_with("/cti_profiles/{}".format(cti_profile_id))
        assert_that(result, has_entries(id=cti_profile_id,
                                        name='client'))
