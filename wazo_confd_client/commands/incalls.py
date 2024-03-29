# Copyright 2016-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import IncallExtensionRelation, IncallScheduleRelation
from wazo_confd_client.util import extract_id


class IncallRelation:
    def __init__(self, builder, incall_id):
        self.incall_id = incall_id
        self.incall_extension = IncallExtensionRelation(builder)
        self.incall_schedule = IncallScheduleRelation(builder)

    @extract_id
    def add_extension(self, extension_id):
        return self.incall_extension.associate(self.incall_id, extension_id)

    @extract_id
    def remove_extension(self, extension_id):
        return self.incall_extension.dissociate(self.incall_id, extension_id)

    @extract_id
    def add_schedule(self, schedule_id):
        return self.incall_schedule.associate(self.incall_id, schedule_id)

    @extract_id
    def remove_schedule(self, schedule_id):
        return self.incall_schedule.dissociate(self.incall_id, schedule_id)


class IncallsCommand(MultiTenantCommand):
    resource = 'incalls'
    relation_cmd = IncallRelation
