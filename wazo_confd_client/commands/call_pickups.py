# -*- coding: utf-8 -*-
# Copyright 2018-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import (
    CallPickupInterceptorGroupRelation,
    CallPickupInterceptorUserRelation,
    CallPickupTargetGroupRelation,
    CallPickupTargetUserRelation,
)


class CallPickupRelation(object):

    def __init__(self, builder, call_pickup_id):
        self.call_pickup_id = call_pickup_id
        self.call_pickup_group_interceptors = CallPickupInterceptorGroupRelation(builder)
        self.call_pickup_group_targets = CallPickupTargetGroupRelation(builder)
        self.call_pickup_user_interceptors = CallPickupInterceptorUserRelation(builder)
        self.call_pickup_user_targets = CallPickupTargetUserRelation(builder)

    def update_group_targets(self, groups):
        return self.call_pickup_group_targets.associate(self.call_pickup_id, groups)

    def update_group_interceptors(self, groups):
        return self.call_pickup_group_interceptors.associate(self.call_pickup_id, groups)

    def update_user_targets(self, users):
        return self.call_pickup_user_targets.associate(self.call_pickup_id, users)

    def update_user_interceptors(self, users):
        return self.call_pickup_user_interceptors.associate(self.call_pickup_id, users)


class CallPickupsCommand(MultiTenantCommand):

    resource = 'callpickups'
    relation_cmd = CallPickupRelation
