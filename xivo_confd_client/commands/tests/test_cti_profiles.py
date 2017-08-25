# -*- coding: utf-8 -*-

# Copyright (C) 2014-2015 Avencall
#
# SPDX-License-Identifier: GPL-3.0+

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
