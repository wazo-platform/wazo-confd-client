# -*- coding: utf-8 -*-
# Copyright 2016-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import MultiTenantCommand
from xivo_confd_client.relations import (
    OutcallCallPermissionRelation,
    OutcallExtensionRelation,
    OutcallScheduleRelation,
    OutcallTrunkRelation,
)


class OutcallRelation(object):

    def __init__(self, builder, outcall_id):
        self.outcall_id = outcall_id
        self.outcall_call_permission = OutcallCallPermissionRelation(builder)
        self.outcall_schedule = OutcallScheduleRelation(builder)
        self.outcall_trunk = OutcallTrunkRelation(builder)
        self.outcall_extension = OutcallExtensionRelation(builder)

    def update_trunks(self, trunks):
        return self.outcall_trunk.associate(self.outcall_id, trunks)

    @extract_id
    def add_extension(self, extension_id, **kwargs):
        return self.outcall_extension.associate(self.outcall_id, extension_id, **kwargs)

    @extract_id
    def remove_extension(self, extension_id):
        return self.outcall_extension.dissociate(self.outcall_id, extension_id)

    @extract_id
    def add_schedule(self, schedule_id):
        return self.outcall_schedule.associate(self.outcall_id, schedule_id)

    @extract_id
    def remove_schedule(self, schedule_id):
        return self.outcall_schedule.dissociate(self.outcall_id, schedule_id)

    @extract_id
    def add_call_permission(self, call_permission_id):
        return self.outcall_call_permission.associate(self.outcall_id, call_permission_id)

    @extract_id
    def remove_call_permission(self, call_permission_id):
        self.outcall_call_permission.dissociate(self.outcall_id, call_permission_id)


class OutcallsCommand(MultiTenantCommand):

    resource = 'outcalls'
    relation_cmd = OutcallRelation
