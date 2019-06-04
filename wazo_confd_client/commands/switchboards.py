# -*- coding: utf-8 -*-
# Copyright 2017-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import SwitchboardMemberUserRelation


class SwitchboardRelation(object):

    def __init__(self, builder, switchboard_id):
        self.switchboard_id = switchboard_id
        self.switchboard_user_members = SwitchboardMemberUserRelation(builder)

    def update_user_members(self, users):
        return self.switchboard_user_members.associate(self.switchboard_id, users)


class SwitchboardsCommand(MultiTenantCommand):

    resource = 'switchboards'
    relation_cmd = SwitchboardRelation
