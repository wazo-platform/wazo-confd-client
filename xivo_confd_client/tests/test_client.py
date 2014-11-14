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

import subprocess
import unittest
import os
import time

from hamcrest import assert_that
from hamcrest import equal_to
from xivo_confd_client import Client


class TestClient(unittest.TestCase):

    def setUp(self):
        os.chdir(os.path.dirname(__file__))
        cmd = ['python', '-m', 'SimpleHTTPServer']
        self._server = subprocess.Popen(cmd)
        time.sleep(1)

    def tearDown(self):
        self._server.terminate()

    def test_client_infos_get(self):
        '''
        This is an integration test to test that the client/plugin system is working.
        You should install the info command to get this test working
        '''
        c = Client('localhost', 8000, '1.1')

        result = c.infos()

        assert_that(result, equal_to({'uuid': 'my-test-uuid'}))
