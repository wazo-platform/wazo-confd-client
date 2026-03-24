# Copyright 2026 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from typing import Any

from wazo_lib_rest_client import HTTPCommand

from wazo_confd_client.util import url_join


class VoicemailTranscriptionCommand(HTTPCommand):
    resource = 'voicemails/transcription'

    def get(self, **kwargs: Any) -> dict[str, Any]:
        tenant_uuid = kwargs.pop('tenant_uuid', None)
        headers = dict(self.session.READ_HEADERS)
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = url_join(self.resource)
        response = self.session.get(url, headers=headers, params=kwargs)
        return response.json()

    def update(self, body: dict[str, Any], **kwargs: Any) -> None:
        tenant_uuid = kwargs.pop('tenant_uuid', None)
        headers = dict(self.session.WRITE_HEADERS)
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        url = url_join(self.resource)
        self.session.put(url, json=body, headers=headers, params=kwargs)
