# -*- coding: utf-8 -*-

# Copyright (C) 2014-2015 Avencall
#
# SPDX-License-Identifier: GPL-3.0+

from ..infos import InfosCommand
from hamcrest import assert_that
from hamcrest import equal_to
from xivo_confd_client.tests import TestCommand


class TestInfos(TestCommand):

    Command = InfosCommand

    def test_get(self):
        self.set_response('get', 200, {'uuid': 'test'})

        result = self.command.get()

        self.session.get.assert_called_once_with('/infos')
        assert_that(result, equal_to({'uuid': 'test'}))

    def test_calling_infos_with_no_method(self):
        self.set_response('get', 200, {'uuid': 'test'})

        result = self.command()

        self.session.get.assert_called_once_with('/infos')
        assert_that(result, equal_to({'uuid': 'test'}))
