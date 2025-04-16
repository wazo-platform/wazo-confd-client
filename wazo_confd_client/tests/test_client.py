# Copyright 2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest

from wazo_lib_rest_client.client import PLUGINS_CACHE

from wazo_confd_client.client import ConfdClient


class TestClient(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ConfdClient('http://localhost/1.1')

    def test_plugins(self) -> None:
        assert PLUGINS_CACHE
        assert self.client.namespace in PLUGINS_CACHE
        assert PLUGINS_CACHE[self.client.namespace]
        assert all(
            hasattr(self.client, plugin.name)
            for plugin in PLUGINS_CACHE[self.client.namespace]
        )
