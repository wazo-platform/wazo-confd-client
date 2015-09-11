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

import unittest

from xivo_confd_client.relations import UserVoicemailRelation
from xivo_confd_client.commands.voicemails import VoicemailRelation

from mock import Mock


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
