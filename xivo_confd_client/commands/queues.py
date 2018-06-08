# -*- coding: utf-8 -*-
# Copyright 2015-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.util import url_join


class QueuesCommand(CRUDCommand):

    resource = 'queues'

    def add_agent(self, queue_id, agent_id, penalty=0):
        url = url_join('queues', queue_id, 'members', 'agents')
        body = {'agent_id': agent_id,
                'penalty': penalty}
        response = self.session.post(url, body)
        return response.json()

    def remove_agent(self, queue_id, agent_id):
        url = url_join('queues', queue_id, 'members', 'agents', agent_id)
        self.session.delete(url)

    def get_membership(self, queue_id, agent_id):
        url = url_join('queues', queue_id, 'members', 'agents', agent_id)
        response = self.session.get(url)
        return response.json()

    def edit_membership(self, queue_id, agent_id, penalty):
        url = url_join('queues', queue_id, 'members', 'agents', agent_id)
        body = {'penalty': penalty}
        self.session.put(url, body)
