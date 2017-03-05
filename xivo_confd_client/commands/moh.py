# -*- coding: utf-8 -*-

# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.util import extract_id, url_join


class MOHCommand(CRUDCommand):

    resource = 'moh'

    @extract_id
    def download_file(self, moh_uuid, filename):
        url = url_join(self.resource, moh_uuid, 'files', filename)
        headers = {'Accept': '*/*'}
        response = self.session.get(url, headers=headers)
        return response.content

    @extract_id
    def upload_file(self, moh_uuid, filename, content):
        url = url_join(self.resource, moh_uuid, 'files', filename)
        headers = {'Content-Type': 'application/octet-stream'}
        self.session.put(url, raw=content, headers=headers)

    @extract_id
    def delete_file(self, moh_uuid, filename):
        url = url_join(self.resource, moh_uuid, 'files', filename)
        self.session.delete(url)
