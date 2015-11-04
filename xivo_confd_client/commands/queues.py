# -*- coding: UTF-8 -*-

# Copyright (C) 2015 Avencall
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from xivo_lib_rest_client import HTTPCommand
from xivo_confd_client.util import url_join


class QueuesCommand(HTTPCommand):

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
