# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import CRUDCommand, MultiTenantCommand
from wazo_confd_client.util import url_join


class UsersMeMeetingsAuthorizationsCommand(MultiTenantCommand):
    def __init__(self, client, meeting_uuid):
        super().__init__(client)
        self._resource = url_join(
            'users', 'me', 'meetings', meeting_uuid, 'authorizations'
        )
        self.meeting_uuid = meeting_uuid

    @property
    def resource(self):
        return self._resource

    def accept(self, authorization_uuid):
        url = url_join(
            'users',
            'me',
            'meetings',
            self.meeting_uuid,
            'authorizations',
            authorization_uuid,
            'accept',
        )
        self.session.put(url)

    def reject(self, authorization_uuid):
        url = url_join(
            'users',
            'me',
            'meetings',
            self.meeting_uuid,
            'authorizations',
            authorization_uuid,
            'reject',
        )
        self.session.put(url)


class UsersMeMeetingsRelation(CRUDCommand):
    def __init__(self, client, meeting_uuid):
        super().__init__(client)
        self.authorizations = UsersMeMeetingsAuthorizationsCommand(client, meeting_uuid)

    @property
    def resource(self):
        return 'users/me/meetings'


class UsersMeMeetingsCommand(MultiTenantCommand):
    resource = 'users/me/meetings'
    relation_cmd = UsersMeMeetingsRelation
