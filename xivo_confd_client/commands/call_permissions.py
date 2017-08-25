# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
#
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.util import extract_id
from xivo_confd_client.relations import UserCallPermissionRelation


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

    def list_users(self):
        return self.user_call_permission.list_by_call_permission(self.call_permission_id)


class CallPermissionsCommand(CRUDCommand):

    resource = 'callpermissions'
    relation_cmd = CallPermissionRelation
