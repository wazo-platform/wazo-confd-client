# -*- coding: utf-8 -*-
# Copyright 2015-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest

from mock import Mock

from xivo_confd_client.relations import UserVoicemailRelation
from xivo_confd_client.commands.voicemails import VoicemailRelation


class TestVoicemailRelation(unittest.TestCase):

    def setUp(self):
        self.voicemail_id = 1
        self.relation = VoicemailRelation(Mock(), self.voicemail_id)
        self.association = self.relation.user_voicemail_relation = Mock(UserVoicemailRelation)

    def test_remove_users(self):
        user_id1 = 11
        user_id2 = 12

        response = {'total': 2,
                    'items': [
                        {'user_id': user_id1,
                         'voicemail_id': self.voicemail_id,
                         'links': [
                             {'rel': 'users',
                              'href': 'http://localhost/1.1/users/10'},
                             {'rel': 'voicemails',
                              'href': 'http://localhost/1.1/voicemails/1'}
                         ]},
                        {'user_id': user_id2,
                         'voicemail_id': self.voicemail_id,
                         'links': [
                             {'rel': 'users',
                              'href': 'http://localhost/1.1/users/11'},
                             {'rel': 'voicemails',
                              'href': 'http://localhost/1.1/voicemails/1'}
                         ]},
                    ]}

        self.association.list_by_voicemail.return_value = response

        self.relation.remove_users()

        self.association.dissociate.assert_any_call(user_id1)
        self.association.dissociate.assert_any_call(user_id2)
