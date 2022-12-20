# Copyright 2016-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import ContextContextRelation


class ContextRelation:
    def __init__(self, builder, context_id):
        self.context_id = context_id
        self.context_context = ContextContextRelation(builder)

    def update_contexts(self, contexts):
        return self.context_context.associate(self.context_id, contexts)


class ContextsCommand(MultiTenantCommand):

    resource = 'contexts'
    relation_cmd = ContextRelation
