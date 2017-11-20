# -*- coding: UTF-8 -*-
# Copyright (C) 2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

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
