# Copyright 2026 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that, equal_to

from wazo_confd_client.session import ConfdSession
from wazo_confd_client.tests import TestCommand

from ..voicemail_transcription import VoicemailTranscriptionCommand

READ_HEADERS = dict(ConfdSession.READ_HEADERS)
WRITE_HEADERS = dict(ConfdSession.WRITE_HEADERS)


class TestVoicemailTranscription(TestCommand):
    Command = VoicemailTranscriptionCommand

    def test_get(self):
        self.client.tenant_uuid = None
        expected = self.set_response('get', 200, {'enabled': True})

        result = self.command.get()

        assert_that(result, equal_to(expected))
        self.session.get.assert_called_once_with(
            '/voicemails/transcription',
            headers=READ_HEADERS,
            params={},
        )

    def test_get_with_tenant_uuid(self):
        self.client.tenant_uuid = None
        expected_headers = {**READ_HEADERS, 'Wazo-Tenant': 'my-tenant-uuid'}
        self.set_response('get', 200, {'enabled': False})

        self.command.get(tenant_uuid='my-tenant-uuid')

        self.session.get.assert_called_once_with(
            '/voicemails/transcription',
            headers=expected_headers,
            params={},
        )

    def test_get_uses_client_tenant_uuid(self):
        self.client.tenant_uuid = 'client-tenant'
        expected_headers = {**READ_HEADERS, 'Wazo-Tenant': 'client-tenant'}
        self.set_response('get', 200, {'enabled': True})

        self.command.get()

        self.session.get.assert_called_once_with(
            '/voicemails/transcription',
            headers=expected_headers,
            params={},
        )

    def test_update(self):
        self.client.tenant_uuid = None
        self.set_response('put', 204)
        body = {'enabled': True}

        self.command.update(body)

        self.session.put.assert_called_once_with(
            '/voicemails/transcription',
            json=body,
            headers=WRITE_HEADERS,
            params={},
        )

    def test_update_with_tenant_uuid(self):
        self.client.tenant_uuid = None
        expected_headers = {**WRITE_HEADERS, 'Wazo-Tenant': 'my-tenant-uuid'}
        self.set_response('put', 204)
        body = {'enabled': True}

        self.command.update(body, tenant_uuid='my-tenant-uuid')

        self.session.put.assert_called_once_with(
            '/voicemails/transcription',
            json=body,
            headers=expected_headers,
            params={},
        )

    def test_update_uses_client_tenant_uuid(self):
        self.client.tenant_uuid = 'client-tenant'
        expected_headers = {**WRITE_HEADERS, 'Wazo-Tenant': 'client-tenant'}
        self.set_response('put', 204)
        body = {'enabled': True}

        self.command.update(body)

        self.session.put.assert_called_once_with(
            '/voicemails/transcription',
            json=body,
            headers=expected_headers,
            params={},
        )
