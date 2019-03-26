# -*- coding: utf-8 -*-
# Copyright 2015-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import MultiTenantCommand

from xivo_confd_client.relations import (
    QueueExtensionRelation,
    QueueFallbackRelation,
    QueueScheduleRelation,
    QueueMemberAgentRelation,
    QueueMemberUserRelation,
)


class QueueRelation(object):

    def __init__(self, builder, queue_id):
        self.queue_id = queue_id
        self.queue_member_agent = QueueMemberAgentRelation(builder)
        self.queue_member_user = QueueMemberUserRelation(builder)
        self.queue_extension = QueueExtensionRelation(builder)
        self.queue_fallback = QueueFallbackRelation(builder)
        self.queue_schedule = QueueScheduleRelation(builder)

    @extract_id
    def add_extension(self, extension_id):
        return self.queue_extension.associate(self.queue_id, extension_id)

    @extract_id
    def remove_extension(self, extension_id):
        return self.queue_extension.dissociate(self.queue_id, extension_id)

    def update_fallbacks(self, fallbacks):
        self.queue_fallback.update_fallbacks(self.queue_id, fallbacks)

    def list_fallbacks(self):
        return self.queue_fallback.list_fallbacks(self.queue_id)

    @extract_id
    def add_schedule(self, schedule_id):
        return self.queue_schedule.associate(self.queue_id, schedule_id)

    @extract_id
    def remove_schedule(self, schedule_id):
        return self.queue_schedule.dissociate(self.queue_id, schedule_id)

    @extract_id
    def add_agent_member(self, agent_id, **kwargs):
        return self.queue_member_agent.associate(self.queue_id, agent_id, **kwargs)

    @extract_id
    def remove_agent_member(self, agent_id):
        return self.queue_member_agent.dissociate(self.queue_id, agent_id)

    @extract_id
    def add_user_member(self, user_uuid, **kwargs):
        return self.queue_member_user.associate(self.queue_id, user_uuid, **kwargs)

    @extract_id
    def remove_user_member(self, user_uuid):
        return self.queue_member_user.dissociate(self.queue_id, user_uuid)


class QueuesCommand(MultiTenantCommand):

    resource = 'queues'
    relation_cmd = QueueRelation
