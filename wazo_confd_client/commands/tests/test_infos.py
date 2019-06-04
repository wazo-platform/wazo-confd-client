# -*- coding: utf-8 -*-
# Copyright 2014-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import (
    assert_that,
    equal_to,
)
from wazo_confd_client.tests import TestCommand

from ..infos import InfosCommand


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
