# -*- coding: utf-8 -*-
# Copyright 2015-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.util import extract_id
from wazo_confd_client.util import url_join
from wazo_confd_client.relations import LineDeviceRelation
from wazo_lib_rest_client import RESTCommand


class DeviceRelation(object):

    def __init__(self, builder, device_id):
        self.device_id = device_id
        self.line_device = LineDeviceRelation(builder)

    @extract_id
    def add_line(self, line_id):
        return self.line_device.associate(line_id, self.device_id)

    @extract_id
    def remove_line(self, line_id):
        return self.line_device.dissociate(line_id, self.device_id)

    def list_lines(self):
        return self.line_device.list_by_device(self.device_id)


class DevicesCommand(MultiTenantCommand):

    resource = 'devices'
    relation_cmd = DeviceRelation

    @extract_id
    def autoprov(self, device_id, **kwargs):
        tenant_uuid = kwargs.pop('tenant_uuid', self._client.tenant())
        headers = dict(kwargs.get('headers', self.session.READ_HEADERS))
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = url_join(self.resource, device_id, 'autoprov')
        self.session.get(url, headers=headers)

    @extract_id
    def synchronize(self, device_id, **kwargs):
        tenant_uuid = kwargs.pop('tenant_uuid', self._client.tenant())
        headers = dict(kwargs.get('headers', self.session.READ_HEADERS))
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = url_join(self.resource, device_id, 'synchronize')
        self.session.get(url, headers=headers)


class UnallocatedDevicesCommand(RESTCommand):

    resource = 'devices/unallocated'

    def list(self, **kwargs):
        url = url_join(self.resource)
        response = self.session.get(url, params=kwargs)
        return response.json()

    def assign_tenant(self, device_id, **kwargs):
        tenant_uuid = kwargs.pop('tenant_uuid', self._client.tenant())
        headers = dict(kwargs.get('headers', self.session.WRITE_HEADERS))
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = url_join(self.resource, device_id)
        response = self.session.put(url, headers=headers)
