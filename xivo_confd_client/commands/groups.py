# -*- coding: utf-8 -*-

# Copyright (C) 2016 Proformatique Inc.
#
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import (GroupExtensionRelation,
                                         GroupFallbackRelation,
                                         GroupMemberUserRelation)


class GroupRelation(object):

    def __init__(self, builder, group_id):
        self.group_id = group_id
        self.group_extension = GroupExtensionRelation(builder)
        self.group_user_members = GroupMemberUserRelation(builder)
        self.group_fallback = GroupFallbackRelation(builder)

    def update_user_members(self, users):
        return self.group_user_members.associate(self.group_id, users)

    @extract_id
    def add_extension(self, extension_id):
        return self.group_extension.associate(self.group_id, extension_id)

    @extract_id
    def remove_extension(self, extension_id):
        return self.group_extension.dissociate(self.group_id, extension_id)

    def update_fallbacks(self, fallbacks):
        self.group_fallback.update_fallbacks(self.group_id, fallbacks)

    def list_fallbacks(self):
        return self.group_fallback.list_fallbacks(self.group_id)


class GroupsCommand(CRUDCommand):

    resource = 'groups'
    relation_cmd = GroupRelation
