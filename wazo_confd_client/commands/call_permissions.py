# -*- coding: utf-8 -*-
# Copyright 2016-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.util import extract_id
from wazo_confd_client.relations import UserCallPermissionRelation


class CallPermissionRelation(object):
    def __init__(self, builder, call_permission_id):
        self.call_permission_id = call_permission_id
        self.user_call_permission = UserCallPermissionRelation(builder)

    @extract_id
    def add_user(self, user_id):
        return self.user_call_permission.associate(user_id, self.call_permission_id)

    @extract_id
    def remove_user(self, user_id):
        return self.user_call_permission.dissociate(user_id, self.call_permission_id)


class CallPermissionsCommand(MultiTenantCommand):

    resource = 'callpermissions'
    relation_cmd = CallPermissionRelation
