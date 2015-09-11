# -*- coding: UTF-8 -*-

# Copyright (C) 2015 Avencall
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from xivo_lib_rest_client import HTTPCommand
from xivo_confd_client.util import url_join


class UserLineRelation(HTTPCommand):

    def associate(self, user_id, line_id):
        url = url_join('users', user_id, 'lines')
        body = {'line_id': line_id}
        return self.session.post(url, body)

    def dissociate(self, user_id, line_id):
        url = url_join('users', user_id, 'lines', line_id)
        self.session.delete(url)

    def list_by_user(self, user_id):
        url = url_join('users', user_id, 'lines')
        response = self.session.get(url)
        return response.json()


class UserVoicemailRelation(HTTPCommand):

    def associate(self, user_id, voicemail_id):
        url = url_join('users', user_id, 'voicemail')
        body = {'voicemail_id': voicemail_id}
        return self.session.post(url, body)

    def dissociate(self, user_id):
        url = url_join('users', user_id, 'voicemail')
        self.session.delete(url)


class LineExtensionRelation(HTTPCommand):

    def associate(self, line_id, extension_id):
        url = url_join('lines', line_id, 'extensions')
        body = {'extension_id': extension_id}
        return self.session.post(url, body)

    def dissociate(self, line_id, extension_id):
        url = url_join('lines', line_id, 'extensions', extension_id)
        self.session.delete(url)


class ExtensionLineRelation(HTTPCommand):

    def get_line(self, extension_id):
        url = url_join('extensions', extension_id, 'line')
        response = self.session.get(url)
        return response.json()


class UserFuncKeyRelation(HTTPCommand):

    def add_funckey(self, user_id, position, funckey):
        url = url_join('users', user_id, 'funckeys', position)
        self.session.put(url, funckey)

    def remove_funckey(self, user_id, position):
        url = url_join('users', user_id, 'funckeys', position)
        self.session.delete(url)

    def get_funckey(self, user_id, position):
        url = url_join('users', user_id, 'funckeys', position)
        response = self.session.get(url)
        return response.json()

    def list_funckeys(self, user_id):
        url = url_join('users', user_id, 'funckeys')
        response = self.session.get(url)
        return response.json()

    def associate_funckey_template(self, user_id, template_id):
        url = url_join('users', user_id, 'funckeys', 'templates', template_id)
        self.session.put(url)

    def dissociate_funckey_template(self, user_id, template_id):
        url = url_join('users', user_id, 'funckeys', 'templates', template_id)
        self.session.delete(url)
