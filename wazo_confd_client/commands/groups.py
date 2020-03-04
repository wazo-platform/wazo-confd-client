# -*- coding: utf-8 -*-
# Copyright 2016-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.util import extract_id
from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import (
    GroupCallPermissionRelation,
    GroupExtensionRelation,
    GroupFallbackRelation,
    GroupMemberExtensionRelation,
    GroupMemberUserRelation,
    GroupScheduleRelation,
)


class GroupRelation(object):
    def __init__(self, builder, group_id):
        self.group_id = group_id
        self.group_call_permission = GroupCallPermissionRelation(builder)
        self.group_extension = GroupExtensionRelation(builder)
        self.group_user_members = GroupMemberUserRelation(builder)
        self.group_extension_members = GroupMemberExtensionRelation(builder)
        self.group_fallback = GroupFallbackRelation(builder)
        self.group_schedule = GroupScheduleRelation(builder)

    def update_user_members(self, users):
        return self.group_user_members.associate(self.group_id, users)

    def update_extension_members(self, extensions):
        return self.group_extension_members.associate(self.group_id, extensions)

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

    @extract_id
    def add_schedule(self, schedule_id):
        return self.group_schedule.associate(self.group_id, schedule_id)

    @extract_id
    def remove_schedule(self, schedule_id):
        return self.group_schedule.dissociate(self.group_id, schedule_id)

    @extract_id
    def add_call_permission(self, call_permission_id):
        return self.group_call_permission.associate(self.group_id, call_permission_id)

    @extract_id
    def remove_call_permission(self, call_permission_id):
        self.group_call_permission.dissociate(self.group_id, call_permission_id)


class GroupsCommand(MultiTenantCommand):

    resource = 'groups'
    relation_cmd = GroupRelation
