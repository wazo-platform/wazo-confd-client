# -*- coding: utf-8 -*-

# Copyright (C) 2016 Proformatique Inc.
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

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import GroupExtensionRelation, GroupMemberUserRelation


class GroupRelation(object):

    def __init__(self, builder, group_id):
        self.group_id = group_id
        self.group_extension = GroupExtensionRelation(builder)
        self.group_user_members = GroupMemberUserRelation(builder)

    def update_user_members(self, users):
        return self.group_user_members.associate(self.group_id, users)

    @extract_id
    def add_extension(self, extension_id):
        return self.group_extension.associate(self.group_id, extension_id)

    @extract_id
    def remove_extension(self, extension_id):
        return self.group_extension.dissociate(self.group_id, extension_id)


class GroupsCommand(CRUDCommand):

    resource = 'groups'
    relation_cmd = GroupRelation
