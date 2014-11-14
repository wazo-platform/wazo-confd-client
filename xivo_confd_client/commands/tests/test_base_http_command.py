# -*- coding: utf-8 -*-

# Copyright (C) 2014 Avencall
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

import unittest

from ..base_http_command import BaseHTTPCommand
from hamcrest import assert_that
from hamcrest import equal_to


class TestBaseHTTPCommand(unittest.TestCase):

    def test_init_no_resource_specified(self):
        class NoResource(BaseHTTPCommand):
            pass

        self.assertRaises(NotImplementedError,
                          NoResource, host='host', port=1234, version='42', use_https=False)

    def test_resource_url_with_https(self):
        class TestCommand(BaseHTTPCommand):
            resource = 'test'

        c = TestCommand('example.com', 9000, '42', use_https=True)

        assert_that(c.resource_url, equal_to('https://example.com:9000/42/test'))

    def test_resource_url_with_http(self):
        class TestCommand(BaseHTTPCommand):
            resource = 'test'

        c = TestCommand('example.com', 9000, '42', use_https=False)

        assert_that(c.resource_url, equal_to('http://example.com:9000/42/test'))
