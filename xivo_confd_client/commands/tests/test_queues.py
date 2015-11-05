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


from hamcrest import assert_that
from hamcrest import has_entries
from xivo_confd_client.tests import TestCommand

from ..queues import QueuesCommand


class TestInfos(TestCommand):

    Command = QueuesCommand

    def test_add_agent(self):
        queue_id = 1
        agent_id = 2
        expected_url = "/queues/{}/members/agents".format(queue_id)
        expected_body = {'agent_id': agent_id,
                         'penalty': 0}
        expected_response = {'queue_id': queue_id,
                             'agent_id': agent_id,
                             'penalty': 0}

        self.set_response('post', 201, expected_response)

        response = self.command.add_agent(queue_id, agent_id)

        assert_that(response, has_entries(expected_response))
        self.session.post.assert_called_once_with(expected_url, expected_body)

    def test_remove_agent(self):
        queue_id = 1
        agent_id = 2
        expected_url = "/queues/{}/members/agents/{}".format(queue_id, agent_id)

        self.set_response('delete', 204)

        self.command.remove_agent(queue_id, agent_id)

        self.session.delete.assert_called_once_with(expected_url)

    def test_get_membership(self):
        queue_id = 1
        agent_id = 2
        expected_url = "/queues/{}/members/agents/{}".format(queue_id, agent_id)
        expected_response = {'queue_id': queue_id,
                             'agent_id': agent_id,
                             'penalty': 0}

        self.set_response('get', 200, expected_response)

        response = self.command.get_membership(queue_id, agent_id)

        assert_that(response, has_entries(expected_response))
        self.session.get.assert_called_once_with(expected_url)

    def test_edit_membership(self):
        queue_id = 1
        agent_id = 2
        expected_url = "/queues/{}/members/agents/{}".format(queue_id, agent_id)
        expected_response = {'penalty': 1}

        self.set_response('put', 204)

        self.command.edit_membership(queue_id, agent_id, 1)

        self.session.put.assert_called_once_with(expected_url, expected_response)
