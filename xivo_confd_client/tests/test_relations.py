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


from hamcrest import assert_that

from xivo_confd_client.tests import TestCommand
from xivo_confd_client.relations import LineExtensionRelation
from xivo_confd_client.relations import LineDeviceRelation
from xivo_confd_client.relations import LineEndpointSipRelation
from xivo_confd_client.relations import LineEndpointSccpRelation
from xivo_confd_client.relations import LineEndpointCustomRelation
from xivo_confd_client.relations import UserFuncKeyRelation
from xivo_confd_client.relations import UserLineRelation
from xivo_confd_client.relations import UserVoicemailRelation
from xivo_confd_client.relations import UserCtiProfileRelation


class TestUserLineRelation(TestCommand):

    Command = UserLineRelation

    def test_user_line_association(self):
        user_id = 1
        line_id = 2

        expected_result = {
            'user_id': user_id,
            'line_id': line_id,
            'links': [
                {'rel': 'users',
                 'href': 'http://localhost:9486/1.1/users/1'},
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/2'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.associate(user_id, line_id)

        self.session.post.assert_called_once_with("/users/1/lines", {'line_id': line_id})
        assert_that(response, expected_result)

    def test_user_line_dissociation(self):
        user_id = 1
        line_id = 2

        self.command.dissociate(user_id, line_id)
        self.session.delete.assert_called_once_with("/users/1/lines/2")

    def test_user_line_list_by_user(self):
        user_id = 1234
        expected_url = "/users/{}/lines".format(user_id)
        expected_result = {
            "total": 0,
            "items": []
        }

        self.set_response('get', 200, expected_result)

        result = self.command.list_by_user(user_id)

        self.session.get.assert_called_once_with(expected_url)
        assert_that(result, expected_result)

    def test_user_line_list_by_line(self):
        line_id = 1234
        expected_url = "/lines/{}/users".format(line_id)
        expected_result = {
            "total": 0,
            "items": []
        }

        self.set_response('get', 200, expected_result)

        result = self.command.list_by_line(line_id)

        self.session.get.assert_called_once_with(expected_url)
        assert_that(result, expected_result)


class TestLineExtensionRelation(TestCommand):

    Command = LineExtensionRelation

    def test_line_extension_association(self):
        line_id = 1
        extension_id = 2

        expected_result = {
            'line_id': line_id,
            'extension_id': extension_id,
            'links': [
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/1'},
                {'rel': 'extensions',
                 'href': 'http://localhost:9486/1.1/extensions/1'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.associate(line_id, extension_id)
        self.session.post.assert_called_once_with("/lines/1/extensions", {'extension_id': extension_id})

        assert_that(response, expected_result)

    def test_line_extension_dissociation(self):
        line_id = 1
        extension_id = 2

        self.command.dissociate(line_id, extension_id)
        self.session.delete.assert_called_once_with("/lines/1/extensions/2")

    def test_list_by_line(self):
        line_id = 1
        extension_id = 2

        expected_result = {
            'total': 1,
            'items': [{
                'line_id': line_id,
                'extension_id': extension_id,
                'links': [
                    {'rel': 'lines',
                     'href': 'http://localhost:9486/1.1/lines/1'},
                    {'rel': 'extensions',
                     'href': 'http://localhost:9486/1.1/extensions/2'},
                ]}
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.list_by_line(line_id)
        self.session.get.assert_called_once_with("/lines/1/extensions")

        assert_that(response, expected_result)

    def test_get_by_extension(self):
        line_id = 1
        extension_id = 2

        expected_result = {
            'line_id': line_id,
            'extension_id': extension_id,
            'links': [
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/1'},
                {'rel': 'extensions',
                 'href': 'http://localhost:9486/1.1/extensions/2'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.get_by_extension(extension_id)
        self.session.get.assert_called_once_with("/extensions/2/line")

        assert_that(response, expected_result)


class TestLineDeviceRelation(TestCommand):

    Command = LineDeviceRelation

    def test_line_device_association(self):
        line_id = 1
        device_id = 2

        self.set_response('put', 204)

        self.command.associate(line_id, device_id)
        self.session.put.assert_called_once_with("/lines/1/devices/2")

    def test_line_device_dissociation(self):
        line_id = 1
        device_id = 2

        self.set_response('delete', 204)

        self.command.dissociate(line_id, device_id)
        self.session.delete.assert_called_once_with("/lines/1/devices/2")

    def test_get_by_line(self):
        line_id = 1
        device_id = 2

        expected_result = {
            'line_id': line_id,
            'device_id': device_id,
            'links': [
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/1'},
                {'rel': 'devices',
                 'href': 'http://localhost:9486/1.1/devices/1'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.get_by_line(line_id)
        self.session.get.assert_called_once_with("/lines/1/devices")

        assert_that(response, expected_result)

    def test_list_by_device(self):
        line_id = 1
        device_id = 2

        expected_result = {'total': 1,
                           'items': [
                               {'line_id': line_id,
                                'device_id': device_id,
                                'links': [
                                    {'rel': 'lines',
                                     'href': 'http://localhost:9486/1.1/lines/1'},
                                    {'rel': 'devices',
                                     'href': 'http://localhost:9486/1.1/devices/1'},
                                ]}]}

        self.set_response('get', 200, expected_result)

        response = self.command.list_by_device(device_id)
        self.session.get.assert_called_once_with("/devices/2/lines")

        assert_that(response, expected_result)


class TestLineEndpointSipRelation(TestCommand):

    Command = LineEndpointSipRelation

    def test_line_endpoint_sip_association(self):
        line_id = 1
        sip_id = 2

        self.set_response('put', 204)

        self.command.associate(line_id, sip_id)
        self.session.put.assert_called_once_with("/lines/1/endpoints/sip/2")

    def test_line_endpoint_sip_dissociation(self):
        line_id = 1
        sip_id = 2

        self.set_response('delete', 204)

        self.command.dissociate(line_id, sip_id)
        self.session.delete.assert_called_once_with("/lines/1/endpoints/sip/2")

    def test_get_by_line(self):
        line_id = 1
        sip_id = 2

        expected_result = {
            'line_id': line_id,
            'sip_id': sip_id,
            'links': [
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/1'},
                {'rel': 'endpoints_sip',
                 'href': 'http://localhost:9486/1.1/endpoints/sip/1'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.get_by_line(line_id)
        self.session.get.assert_called_once_with("/lines/1/endpoints/sip")

        assert_that(response, expected_result)

    def test_get_by_endpoint_sip(self):
        line_id = 1
        sip_id = 2

        expected_result = {
            'line_id': line_id,
            'sip_id': sip_id,
            'links': [
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/1'},
                {'rel': 'endpoints_sip',
                 'href': 'http://localhost:9486/1.1/endpoints/sip/1'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.get_by_endpoint_sip(sip_id)
        self.session.get.assert_called_once_with("/endpoints/sip/2/lines")

        assert_that(response, expected_result)


class TestLineEndpointSccpRelation(TestCommand):

    Command = LineEndpointSccpRelation

    def test_line_endpoint_sccp_association(self):
        line_id = 1
        sccp_id = 2

        self.set_response('put', 204)

        self.command.associate(line_id, sccp_id)
        self.session.put.assert_called_once_with("/lines/1/endpoints/sccp/2")

    def test_line_endpoint_sccp_dissociation(self):
        line_id = 1
        sccp_id = 2

        self.set_response('delete', 204)

        self.command.dissociate(line_id, sccp_id)
        self.session.delete.assert_called_once_with("/lines/1/endpoints/sccp/2")

    def test_get_by_line(self):
        line_id = 1
        sccp_id = 2

        expected_result = {
            'line_id': line_id,
            'sccp_id': sccp_id,
            'links': [
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/1'},
                {'rel': 'endpoints_sccp',
                 'href': 'http://localhost:9486/1.1/endpoints/sccp/1'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.get_by_line(line_id)
        self.session.get.assert_called_once_with("/lines/1/endpoints/sccp")

        assert_that(response, expected_result)

    def test_get_by_endpoint_sccp(self):
        line_id = 1
        sccp_id = 2

        expected_result = {
            'line_id': line_id,
            'sccp_id': sccp_id,
            'links': [
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/1'},
                {'rel': 'endpoints_sccp',
                 'href': 'http://localhost:9486/1.1/endpoints/sccp/1'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.get_by_endpoint_sccp(sccp_id)
        self.session.get.assert_called_once_with("/endpoints/sccp/2/lines")

        assert_that(response, expected_result)


class TestLineEndpointCustomRelation(TestCommand):

    Command = LineEndpointCustomRelation

    def test_line_endpoint_custom_association(self):
        line_id = 1
        custom_id = 2

        self.set_response('put', 204)

        self.command.associate(line_id, custom_id)
        self.session.put.assert_called_once_with("/lines/1/endpoints/custom/2")

    def test_line_endpoint_custom_dissociation(self):
        line_id = 1
        custom_id = 2

        self.set_response('delete', 204)

        self.command.dissociate(line_id, custom_id)
        self.session.delete.assert_called_once_with("/lines/1/endpoints/custom/2")

    def test_get_by_line(self):
        line_id = 1
        custom_id = 2

        expected_result = {
            'line_id': line_id,
            'custom_id': custom_id,
            'links': [
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/1'},
                {'rel': 'endpoints_custom',
                 'href': 'http://localhost:9486/1.1/endpoints/custom/1'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.get_by_line(line_id)
        self.session.get.assert_called_once_with("/lines/1/endpoints/custom")

        assert_that(response, expected_result)

    def test_get_by_endpoint_custom(self):
        line_id = 1
        custom_id = 2

        expected_result = {
            'line_id': line_id,
            'custom_id': custom_id,
            'links': [
                {'rel': 'lines',
                 'href': 'http://localhost:9486/1.1/lines/1'},
                {'rel': 'endpoints_custom',
                 'href': 'http://localhost:9486/1.1/endpoints/custom/1'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.get_by_endpoint_custom(custom_id)
        self.session.get.assert_called_once_with("/endpoints/custom/2/lines")

        assert_that(response, expected_result)


class TestUserVoicemailRelation(TestCommand):

    Command = UserVoicemailRelation

    def test_user_voicemail_association(self):
        user_id = 1
        voicemail_id = 2

        expected_result = {
            'user_id': user_id,
            'voicemail_id': voicemail_id,
            'links': [
                {'rel': 'users',
                 'href': 'http://localhost:9486/1.1/users/2'},
                {'rel': 'voicemails',
                 'href': 'http://localhost:9486/1.1/voicemails/1'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.associate(user_id, voicemail_id)

        self.session.post.assert_called_once_with("/users/1/voicemail", {'voicemail_id': voicemail_id})
        assert_that(response, expected_result)

    def test_user_voicemail_dissociation(self):
        user_id = 1

        self.command.dissociate(user_id)
        self.session.delete.assert_called_once_with("/users/1/voicemail")

    def test_get_by_user(self):
        user_id = 1
        expected_result = {
            'user_id': user_id,
            'voicemail_id': 2,
            'links': [
                {'rel': 'users',
                 'href': 'http://localhost:9486/1.1/users/1'},
                {'rel': 'voicemails',
                 'href': 'http://localhost:9486/1.1/voicemails/2'},
            ]
        }

        self.set_response('get', 200, expected_result)

        response = self.command.get_by_user(user_id)

        self.session.get.assert_called_once_with("/users/1/voicemail")
        assert_that(response, expected_result)

    def test_list_by_voicemail(self):
        voicemail_id = 1
        expected_result = {
            'items': [],
            'total': 0
        }

        self.set_response('get', 200, expected_result)

        response = self.command.list_by_voicemail(voicemail_id)

        self.session.get.assert_called_once_with("/voicemails/1/users")
        assert_that(response, expected_result)


class TestUserFuncKeyRelation(TestCommand):

    Command = UserFuncKeyRelation

    def test_add_func_key(self):
        user_id = 1234
        position = 1
        funckey = {'destination': {'type': 'service', 'service': 'enablednd'}}

        self.command.add_funckey(user_id, position, funckey)

        expected_url = "/users/{}/funckeys/{}".format(user_id, position)
        self.session.put.assert_called_with(expected_url, funckey)

    def test_remove_func_key(self):
        user_id = 1234
        position = 1
        expected_url = "/users/{}/funckeys/{}".format(user_id, position)

        self.command.remove_funckey(user_id, position)

        self.session.delete.assert_called_with(expected_url)

    def test_list_funckeys(self):
        user_id = 1234
        expected_url = "/users/{}/funckeys".format(user_id)
        expected_result = {
            "total": 0,
            "items": []
        }

        self.set_response('get', 200, expected_result)

        result = self.command.list_funckeys(user_id)

        self.session.get.assert_called_once_with(expected_url)
        assert_that(result, expected_result)

    def test_get_funckey(self):
        user_id = 1234
        position = 3
        expected_url = "/users/{}/funckeys/{}".format(user_id, position)
        expected_result = {
            "blf": True,
            "label": "Call john",
            "destination": {
                "type": "user",
                "user_id": 34
            }
        }

        self.set_response('get', 200, expected_result)

        result = self.command.get_funckey(user_id, position)

        self.session.get.assert_called_once_with(expected_url)
        assert_that(result, expected_result)

    def test_dissociate_funckey_template(self):
        user_id = 1234
        template_id = 25
        expected_url = "/users/{}/funckeys/templates/{}".format(user_id, template_id)

        self.set_response('delete', 204)

        self.command.dissociate_funckey_template(user_id, template_id)

        self.session.delete.assert_called_once_with(expected_url)

    def test_associate_funckey_template(self):
        user_id = 1234
        template_id = 25
        expected_url = "/users/{}/funckeys/templates/{}".format(user_id, template_id)

        self.set_response('put', 204)

        self.command.associate_funckey_template(user_id, template_id)

        self.session.put.assert_called_once_with(expected_url)


class TestUserCtiProfileRelation(TestCommand):

    Command = UserCtiProfileRelation

    def test_get_by_user(self):
        user_id = 1234
        expected_url = "/users/{}/cti".format(user_id)
        expected_result = {
            'cti_profile_id': 2345,
            'enabled': True,
            'user_id': user_id
        }

        self.set_response('get', 200, expected_result)

        result = self.command.get_by_user(user_id)

        self.session.get.assert_called_once_with(expected_url)
        assert_that(result, expected_result)

    def test_associate(self):
        user_id = 1234
        cti_profile_id = 2345

        expected_url = "/users/{}/cti".format(user_id)
        expected_body = {
            'cti_profile_id': 2345,
            'enabled': True,
        }

        self.set_response('put', 204)

        self.command.associate(user_id, cti_profile_id)

        self.session.put.assert_called_once_with(expected_url, expected_body)

    def test_disable(self):
        user_id = 1234

        expected_url = "/users/{}/cti".format(user_id)
        expected_body = {
            'enabled': False,
        }

        self.set_response('put', 204)

        self.command.disable(user_id)

        self.session.put.assert_called_once_with(expected_url, expected_body)
