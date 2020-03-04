# -*- coding: utf-8 -*-
# Copyright 2015-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.util import extract_id
from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import UserVoicemailRelation


class VoicemailRelation(object):
    def __init__(self, builder, voicemail_id):
        self.voicemail_id = voicemail_id
        self.user_voicemail_relation = UserVoicemailRelation(builder)

    @extract_id
    def add_user(self, user_id):
        self.user_voicemail_relation.associate(user_id, self.voicemail_id)

    @extract_id
    def remove_user(self, user_id):
        self.user_voicemail_relation.dissociate(user_id)

    def remove_users(self):
        response = self.list_users()
        for association in response['items']:
            self.remove_user(association['user_id'])

    def list_users(self):
        return self.user_voicemail_relation.list_by_voicemail(self.voicemail_id)


class VoicemailsCommand(MultiTenantCommand):

    resource = 'voicemails'

    relation_cmd = VoicemailRelation
