# -*- coding: utf-8 -*-
# Copyright 2017-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.crud import MultiTenantCommand
from xivo_confd_client.util import extract_id, url_join


class MOHCommand(MultiTenantCommand):

    resource = 'moh'

    @extract_id
    def download_file(self, moh_uuid, filename):
        url = url_join(self.resource, moh_uuid, 'files', filename)
        headers = {'Accept': '*/*'}
        response = self.session.get(url, headers=headers)
        return response

    @extract_id
    def upload_file(self, moh_uuid, filename, content):
        url = url_join(self.resource, moh_uuid, 'files', filename)
        headers = {'Content-Type': 'application/octet-stream'}
        self.session.put(url, raw=content, headers=headers)

    @extract_id
    def delete_file(self, moh_uuid, filename):
        url = url_join(self.resource, moh_uuid, 'files', filename)
        self.session.delete(url)
