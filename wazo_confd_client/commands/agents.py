# Copyright 2018-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.util import extract_id
from wazo_confd_client.crud import MultiTenantCommand

from wazo_confd_client.relations import AgentSkillRelation


class AgentRelation:
    def __init__(self, builder, agent_id):
        self.agent_id = agent_id
        self.agent_skill = AgentSkillRelation(builder)

    @extract_id
    def add_skill(self, skill_id, **kwargs):
        return self.agent_skill.associate(self.agent_id, skill_id, **kwargs)

    @extract_id
    def remove_skill(self, skill_id):
        return self.agent_skill.dissociate(self.agent_id, skill_id)


class AgentsCommand(MultiTenantCommand):

    resource = 'agents'
    relation_cmd = AgentRelation
