# -*- coding: utf-8 -*-
# Copyright 2015-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_confd_client.tests import TestCommand

from ..devices import DevicesCommand


class TestDevices(TestCommand):

    Command = DevicesCommand

    def test_autoprov(self):
        device_id = "a1b2c3d4e5f6g7h8i9j0k1l2"
        expected_url = "/devices/{}/autoprov".format(device_id)
        expected_headers = {
            'Accept': 'application/json',
        }
        self.client.tenant.return_value = None
        self.set_response('get', 204)

        self.command.autoprov(device_id)

        self.session.get.assert_called_once_with(expected_url, headers=expected_headers)

    def test_autoprov_with_tenant(self):
        device_id = "a1b2c3d4e5f6g7h8i9j0k1l2"
        expected_url = "/devices/{}/autoprov".format(device_id)
        expected_headers = {
            'Accept': 'application/json',
            'Wazo-Tenant': 'tenant',
        }
        self.client.tenant.return_value = 'tenant'
        self.set_response('get', 204)

        self.command.autoprov(device_id)

        self.session.get.assert_called_once_with(expected_url, headers=expected_headers)

    def test_synchronize(self):
        device_id = "a1b2c3d4e5f6g7h8i9j0k1l2"
        expected_url = "/devices/{}/synchronize".format(device_id)
        expected_headers = {
            'Accept': 'application/json',
        }
        self.client.tenant.return_value = None
        self.set_response('get', 204)

        self.command.synchronize(device_id)

        self.session.get.assert_called_once_with(expected_url, headers=expected_headers)

    def test_synchronize_with_tenants(self):
        device_id = "a1b2c3d4e5f6g7h8i9j0k1l2"
        expected_url = "/devices/{}/synchronize".format(device_id)
        expected_headers = {
            'Accept': 'application/json',
            'Wazo-Tenant': 'tenant',
        }
        self.client.tenant.return_value = 'tenant'
        self.set_response('get', 204)

        self.command.synchronize(device_id)

        self.session.get.assert_called_once_with(expected_url, headers=expected_headers)
