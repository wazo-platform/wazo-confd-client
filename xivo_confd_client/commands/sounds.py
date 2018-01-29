# -*- coding: utf-8 -*-
# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from six.moves.urllib.parse import quote

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.util import extract_id, url_join


class SoundsCommand(CRUDCommand):

    resource = 'sounds'

    @extract_id
    def download_file(self, category, filename, **kwargs):
        url = url_join(self.resource, category, 'files', quote(filename, safe=''))
        headers = {'Accept': '*/*'}
        response = self.session.get(url, headers=headers, params=kwargs)
        return response

    @extract_id
    def upload_file(self, category, filename, content, **kwargs):
        url = url_join(self.resource, category, 'files', filename)
        headers = {'Content-Type': 'application/octet-stream'}
        self.session.put(url, raw=content, headers=headers, params=kwargs)

    @extract_id
    def delete_file(self, category, filename, **kwargs):
        url = url_join(self.resource, category, 'files', filename)
        self.session.delete(url, params=kwargs)
