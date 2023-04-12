# Copyright 2022-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.util import url_join


class GuestsMeetingsAuthorizationsCommand(MultiTenantCommand):
    def __init__(self, client, guest_and_meeting_uuid):
        super().__init__(client)
        guest_uuid, meeting_uuid = guest_and_meeting_uuid
        self._resource = url_join(
            'guests', guest_uuid, 'meetings', meeting_uuid, 'authorizations'
        )

    @property
    def resource(self):
        return self._resource


class GuestsMeetingsRelation:
    def __init__(self, builder, guest_and_meeting_uuid):
        self.authorizations = GuestsMeetingsAuthorizationsCommand(
            builder, guest_and_meeting_uuid
        )


class GuestsMeetingsCommand(MultiTenantCommand):
    resource = ['meetings']
    relation_cmd = GuestsMeetingsRelation

    def __init__(self, client, guest_uuid):
        super().__init__(client)
        self.guest_uuid = guest_uuid

    def relations(self, meeting_uuid):
        return super().relations((self.guest_uuid, meeting_uuid))


class GuestsRelation:
    def __init__(self, builder, guest_uuid):
        self.guest_uuid = guest_uuid
        self.meetings = GuestsMeetingsCommand(builder, guest_uuid)


class GuestsCommand(MultiTenantCommand):
    resource = ['guests']
    relation_cmd = GuestsRelation
