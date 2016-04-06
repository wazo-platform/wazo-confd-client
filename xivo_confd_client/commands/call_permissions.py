# -*- coding: utf-8 -*-

# Copyright (C) 2016 Avencall
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
        return self.user_call_permission.get_by_call_permission(self.call_permission_id)


class CallPermissionsCommand(CRUDCommand):

    resource = 'callpermissions'
    relation_cmd = CallPermissionRelation
