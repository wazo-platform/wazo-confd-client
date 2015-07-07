# -*- coding: utf-8 -*-

# Copyright (C) 2014-2015 Avencall
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


class UsersCommand(BaseHTTPCommand):

    resource = 'users'
    read_only_headers = {'Accept': 'application/json'}
    read_write_headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def list(self, **kwargs):
        r = self.session.get(self.base_url, params=kwargs, headers=self.read_only_headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def list_funckeys(self, user_id, **kwargs):
        url = '{base_url}/{user_id}/funckeys'.format(base_url=self.base_url,
                                                     user_id=user_id)

        r = self.session.get(url, params=kwargs, headers=self.read_only_headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def delete_funckeys(self, user_id, **kwargs):
        url = '{base_url}/{user_id}/funckeys'.format(base_url=self.base_url,
                                                     user_id=user_id)

        r = self.session.delete(url, params=kwargs, headers=self.read_only_headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def get_funckey(self, user_id, position, **kwargs):
        url = '{base_url}/{user_id}/funckeys/{position}'.format(base_url=self.base_url,
                                                                user_id=user_id,
                                                                position=position)

        r = self.session.get(url, params=kwargs, headers=self.read_only_headers)

        if r.status_code != 200:
            self.raise_from_response(r)

        return r.json()

    def delete_funckey(self, user_id, position, **kwargs):
        url = '{base_url}/{user_id}/funckeys/{position}'.format(base_url=self.base_url,
                                                                user_id=user_id,
                                                                position=position)

        r = self.session.delete(url, params=kwargs, headers=self.read_only_headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def update_funckey(self, user_id, position, data, **kwargs):
        url = '{base_url}/{user_id}/funckeys/{position}'.format(base_url=self.base_url,
                                                                user_id=user_id,
                                                                position=position)

        r = self.session.put(url, params=kwargs, data=json.dumps(data), headers=self.read_write_headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def dissociate_funckey_template(self, user_id, template_id, **kwargs):
        url = '{base_url}/{user_id}/funckeys/templates/{template_id}'.format(base_url=self.base_url,
                                                                             user_id=user_id,
                                                                             template_id=template_id)

        r = self.session.delete(url, params=kwargs, headers=self.read_write_headers)

        if r.status_code != 204:
            self.raise_from_response(r)

    def associate_funckey_template(self, user_id, template_id, **kwargs):
        url = '{base_url}/{user_id}/funckeys/templates/{template_id}'.format(base_url=self.base_url,
                                                                             user_id=user_id,
                                                                             template_id=template_id)

        r = self.session.put(url, params=kwargs, headers=self.read_write_headers)

        if r.status_code != 204:
            self.raise_from_response(r)
