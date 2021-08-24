# -*- coding: utf-8 -*-
# Copyright 2017-2021 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import (
    SwitchboardFallbackRelation,
    SwitchboardMemberUserRelation,
)


class SwitchboardRelation(object):
    def __init__(self, builder, switchboard_id):
        self.switchboard_id = switchboard_id
        self.switchboard_user_members = SwitchboardMemberUserRelation(builder)
        self.switchboard_fallback = SwitchboardFallbackRelation(builder)

    def update_user_members(self, users):
        return self.switchboard_user_members.associate(self.switchboard_id, users)

    def update_fallbacks(self, fallbacks):
        self.switchboard_fallback.update_fallbacks(self.switchboard_id, fallbacks)

    def list_fallbacks(self):
        return self.switchboard_fallback.list_fallbacks(self.switchboard_id)


class SwitchboardsCommand(MultiTenantCommand):

    resource = 'switchboards'
    relation_cmd = SwitchboardRelation
