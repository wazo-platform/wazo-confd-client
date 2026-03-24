# Copyright 2026 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

from typing import Any

from wazo_confd_client.crud import TenantConfigCommand
from wazo_confd_client.util import url_join


class VoicemailTranscriptionCommand(TenantConfigCommand):
    resource = 'voicemails/transcription'

    def get(self, **kwargs: Any) -> dict[str, Any]:
        headers, kwargs = self._get_read_headers(**kwargs)
        url = url_join(self.resource)
        response = self.session.get(url, headers=headers, params=kwargs)
        return response.json()

    def update(self, body: dict[str, Any], **kwargs: Any) -> None:
        headers, kwargs = self._get_write_headers(**kwargs)
        url = url_join(self.resource)
        self.session.put(url, json=body, headers=headers, params=kwargs)
