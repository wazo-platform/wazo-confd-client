# -*- coding: utf-8 -*-
# Copyright (C) 2015-2016 Avencall
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.util import extract_id
from xivo_confd_client.util import url_join
from xivo_confd_client.relations import LineDeviceRelation


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


class DevicesCommand(CRUDCommand):

    resource = 'devices'
    relation_cmd = DeviceRelation

    @extract_id
    def autoprov(self, device_id):
        url = url_join(self.resource, device_id, 'autoprov')
        self.session.get(url)

    @extract_id
    def synchronize(self, device_id):
        url = url_join(self.resource, device_id, 'synchronize')
        self.session.get(url)
