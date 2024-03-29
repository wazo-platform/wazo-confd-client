# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import (
    PagingCallerUserRelation,
    PagingMemberUserRelation,
)


class PagingRelation:
    def __init__(self, builder, paging_id):
        self.paging_id = paging_id
        self.paging_user_callers = PagingCallerUserRelation(builder)
        self.paging_user_members = PagingMemberUserRelation(builder)

    def update_user_members(self, users):
        return self.paging_user_members.associate(self.paging_id, users)

    def update_user_callers(self, users):
        return self.paging_user_callers.associate(self.paging_id, users)


class PagingsCommand(MultiTenantCommand):
    resource = 'pagings'
    relation_cmd = PagingRelation
