# -*- coding: utf-8 -*-
# Copyright (C) 2017 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import SwitchboardMemberUserRelation


class SwitchboardRelation(object):

    def __init__(self, builder, switchboard_id):
        self.switchboard_id = switchboard_id
        self.switchboard_user_members = SwitchboardMemberUserRelation(builder)

    def update_user_members(self, users):
        return self.switchboard_user_members.associate(self.switchboard_id, users)


class SwitchboardsCommand(CRUDCommand):

    resource = 'switchboards'
    relation_cmd = SwitchboardRelation
