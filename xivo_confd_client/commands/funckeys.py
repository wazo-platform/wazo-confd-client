# -*- coding: utf-8 -*-

# Copyright (C) 2014 Avencall
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

from xivo_lib_rest_client import BaseHTTPCommand
import json


class FuncKeysCommand(BaseHTTPCommand):

    resource = 'funckeys'
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def list_templates(self):
        url = '{base_url}/templates'.format(base_url=self.base_url)
        r = self.session.get(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def create_template(self, data):
        url = '{base_url}/templates'.format(base_url=self.base_url)
        r = self.session.post(url,
                              headers=self.headers,
                              data=json.dumps(data))

        if r.status_code != 201:
            self.raise_from_response(r)

    def get_template(self, template_id):
        url = '{base_url}/templates/{template_id}'.format(base_url=self.base_url,
                                                                   template_id=template_id)
        r = self.session.get(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def delete_template(self, template_id):
        url = '{base_url}/templates/{template_id}'.format(base_url=self.base_url,
                                                          template_id=template_id)

        r = self.session.delete(url, headers=self.headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def get_funckey_template(self, template_id, position):
        url = '{base_url}/templates/{template_id}/{position}'.format(base_url=self.base_url,
                                                                     template_id=template_id,
                                                                     position=position)
        r = self.session.get(url, headers=self.headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def delete_funckey_template(self, template_id, position):
        url = '{base_url}/templates/{template_id}/{position}'.format(base_url=self.base_url,
                                                                     template_id=template_id,
                                                                     position=position)

        r = self.session.delete(url, headers=self.headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def update_funckey_template(self, template_id, position, data):
        url = '{base_url}/templates/{template_id}/{position}'.format(base_url=self.base_url,
                                                                     template_id=template_id,
                                                                     position=position)

        r = self.session.put(url,
                             data=json.dumps(data),
                             headers=self.headers)

        if r.status_code != 204:
            self.raise_from_response(r)
