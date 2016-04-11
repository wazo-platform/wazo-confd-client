# -*- coding: UTF-8 -*-

# Copyright (C) 2015-2016 Avencall
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
        response = self.session.post(url, body)
        return response.json()

    def dissociate(self, user_id, line_id):
        url = url_join('users', user_id, 'lines', line_id)
        self.session.delete(url)

    def list_by_user(self, user_id):
        url = url_join('users', user_id, 'lines')
        response = self.session.get(url)
        return response.json()

    def list_by_line(self, line_id):
        url = url_join('lines', line_id, 'users')
        response = self.session.get(url)
        return response.json()


class UserVoicemailRelation(HTTPCommand):

    def associate(self, user_id, voicemail_id):
        url = url_join('users', user_id, 'voicemail')
        body = {'voicemail_id': voicemail_id}
        response = self.session.post(url, body)
        return response.json()

    def dissociate(self, user_id):
        url = url_join('users', user_id, 'voicemail')
        self.session.delete(url)

    def get_by_user(self, user_id):
        url = url_join('users', user_id, 'voicemail')
        response = self.session.get(url)
        return response.json()

    def list_by_voicemail(self, voicemail_id):
        url = url_join('voicemails', voicemail_id, 'users')
        response = self.session.get(url)
        return response.json()


class LineDeviceRelation(HTTPCommand):

    def associate(self, line_id, device_id):
        url = url_join('lines', line_id, 'devices', device_id)
        self.session.put(url)

    def dissociate(self, line_id, device_id):
        url = url_join('lines', line_id, 'devices', device_id)
        self.session.delete(url)

    def get_by_line(self, line_id):
        url = url_join('lines', line_id, 'devices')
        response = self.session.get(url)
        return response.json()

    def list_by_device(self, device_id):
        url = url_join('devices', device_id, 'lines')
        response = self.session.get(url)
        return response.json()


class LineExtensionRelation(HTTPCommand):

    def associate(self, line_id, extension_id):
        url = url_join('lines', line_id, 'extensions')
        body = {'extension_id': extension_id}
        response = self.session.post(url, body)
        return response.json()

    def dissociate(self, line_id, extension_id):
        url = url_join('lines', line_id, 'extensions', extension_id)
        self.session.delete(url)

    def list_by_line(self, line_id):
        url = url_join('lines', line_id, 'extensions')
        response = self.session.get(url)
        return response.json()

    def get_by_extension(self, extension_id):
        url = url_join('extensions', extension_id, 'line')
        response = self.session.get(url)
        return response.json()


class LineEndpointSipRelation(HTTPCommand):

    def associate(self, line_id, sip_id):
        url = url_join('lines', line_id, 'endpoints', 'sip', sip_id)
        self.session.put(url)

    def dissociate(self, line_id, sip_id):
        url = url_join('lines', line_id, 'endpoints', 'sip', sip_id)
        self.session.delete(url)

    def get_by_line(self, line_id):
        url = url_join('lines', line_id, 'endpoints', 'sip')
        response = self.session.get(url)
        return response.json()

    def get_by_endpoint_sip(self, sip_id):
        url = url_join('endpoints', 'sip', sip_id, 'lines')
        response = self.session.get(url)
        return response.json()


class LineEndpointSccpRelation(HTTPCommand):

    def associate(self, line_id, sccp_id):
        url = url_join('lines', line_id, 'endpoints', 'sccp', sccp_id)
        self.session.put(url)

    def dissociate(self, line_id, sccp_id):
        url = url_join('lines', line_id, 'endpoints', 'sccp', sccp_id)
        self.session.delete(url)

    def get_by_line(self, line_id):
        url = url_join('lines', line_id, 'endpoints', 'sccp')
        response = self.session.get(url)
        return response.json()

    def get_by_endpoint_sccp(self, sccp_id):
        url = url_join('endpoints', 'sccp', sccp_id, 'lines')
        response = self.session.get(url)
        return response.json()


class LineEndpointCustomRelation(HTTPCommand):

    def associate(self, line_id, custom_id):
        url = url_join('lines', line_id, 'endpoints', 'custom', custom_id)
        self.session.put(url)

    def dissociate(self, line_id, custom_id):
        url = url_join('lines', line_id, 'endpoints', 'custom', custom_id)
        self.session.delete(url)

    def get_by_line(self, line_id):
        url = url_join('lines', line_id, 'endpoints', 'custom')
        response = self.session.get(url)
        return response.json()

    def get_by_endpoint_custom(self, custom_id):
        url = url_join('endpoints', 'custom', custom_id, 'lines')
        response = self.session.get(url)
        return response.json()


class UserFuncKeyRelation(HTTPCommand):

    def update_funckey(self, user_id, position, funckey):
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


class UserCtiProfileRelation(HTTPCommand):

    def get_by_user(self, user_id):
        url = url_join('users', user_id, 'cti')
        response = self.session.get(url)
        return response.json()

    def associate(self, user_id, cti_profile_id, enabled=True):
        url = url_join('users', user_id, 'cti')
        body = {'cti_profile_id': cti_profile_id,
                'enabled': enabled}
        self.session.put(url, body)

    def disable(self, user_id):
        url = url_join('users', user_id, 'cti')
        body = {'enabled': False}
        self.session.put(url, body)


class UserServiceRelation(HTTPCommand):

    def update_service(self, user_id, service_name, service):
        url = url_join('users', user_id, 'services', service_name)
        self.session.put(url, service)

    def get_service(self, user_id, service_name):
        url = url_join('users', user_id, 'services', service_name)
        response = self.session.get(url)
        return response.json()

    def list_services(self, user_id):
        url = url_join('users', user_id, 'services')
        response = self.session.get(url)
        return response.json()


class UserForwardRelation(HTTPCommand):

    def update_forward(self, user_id, forward_name, forward):
        url = url_join('users', user_id, 'forwards', forward_name)
        self.session.put(url, forward)

    def get_forward(self, user_id, forward_name):
        url = url_join('users', user_id, 'forwards', forward_name)
        response = self.session.get(url)
        return response.json()

    def list_forwards(self, user_id):
        url = url_join('users', user_id, 'forwards')
        response = self.session.get(url)
        return response.json()

    def update_forwards(self, user_id, forwards):
        url = url_join('users', user_id, 'forwards')
        self.session.put(url, forwards)


class UserCallPermissionRelation(HTTPCommand):

    def associate(self, user_id, call_permission_id):
        url = url_join('users', user_id, 'callpermissions', call_permission_id)
        self.session.put(url)

    def dissociate(self, user_id, call_permission_id):
        url = url_join('users', user_id, 'callpermissions', call_permission_id)
        self.session.delete(url)

    def list_by_user(self, user_id):
        url = url_join('users', user_id, 'callpermissions')
        response = self.session.get(url)
        return response.json()

    def list_by_call_permission(self, call_permission_id):
        url = url_join('callpermissions', call_permission_id, 'users')
        response = self.session.get(url)
        return response.json()
