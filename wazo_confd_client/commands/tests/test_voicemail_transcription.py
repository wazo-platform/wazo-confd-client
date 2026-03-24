# Copyright 2026 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from unittest.mock import ANY

from hamcrest import assert_that, equal_to

from wazo_confd_client.tests import TestCommand

from ..voicemail_transcription import VoicemailTranscriptionCommand


class TestVoicemailTranscription(TestCommand):
    Command = VoicemailTranscriptionCommand

    def test_get(self):
        expected = self.set_response('get', 200, {'enabled': True})

        result = self.command.get()

        assert_that(result, equal_to(expected))
        self.session.get.assert_called_once_with(
            '/voicemails/transcription',
            headers=ANY,
            params={},
        )

    def test_get_with_tenant_uuid(self):
        tenant_uuid = 'my-tenant-uuid'
        self.set_response('get', 200, {'enabled': False})

        self.command.get(tenant_uuid=tenant_uuid)

        call_kwargs = self.session.get.call_args
        assert_that(call_kwargs.kwargs['headers']['Wazo-Tenant'], equal_to(tenant_uuid))

    def test_update(self):
        self.set_response('put', 204)
        body = {'enabled': True}

        self.command.update(body)

        self.session.put.assert_called_once_with(
            '/voicemails/transcription',
            json=body,
            headers=ANY,
            params={},
        )

    def test_update_with_tenant_uuid(self):
        tenant_uuid = 'my-tenant-uuid'
        self.set_response('put', 204)
        body = {'enabled': True}

        self.command.update(body, tenant_uuid=tenant_uuid)

        call_kwargs = self.session.put.call_args
        assert_that(call_kwargs.kwargs['headers']['Wazo-Tenant'], equal_to(tenant_uuid))
