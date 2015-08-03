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


from hamcrest import assert_that

from xivo_confd_client.tests import TestCommand
from xivo_confd_client.relations import LineExtensionRelation
from xivo_confd_client.relations import UserFuncKeyRelation
from xivo_confd_client.relations import UserLineRelation
from xivo_confd_client.relations import UserVoicemailRelation


class TestUserLineRelation(TestCommand):

    Command = UserLineRelation

    def test_user_line_association(self):
        user_id = 1
        line_id = 2

        self.command.associate(user_id, line_id)
        self.session.post.assert_called_once_with("/users/1/lines", {'line_id': line_id})

    def test_user_line_dissociation(self):
        user_id = 1
        line_id = 2

        self.command.dissociate(user_id, line_id)
        self.session.delete.assert_called_once_with("/users/1/lines/2")

    def test_user_line_list(self):
        user_id = 1234
        expected_url = "/users/{}/lines".format(user_id)
        expected_result = {
            "total": 0,
            "items": []
        }

        self.set_response('get', 200, expected_result)

        result = self.command.list(user_id)

        self.session.get.assert_called_once_with(expected_url)
        assert_that(result, expected_result)


class TestLineExtensionRelation(TestCommand):

    Command = LineExtensionRelation

    def test_line_extension_association(self):
        line_id = 1
        extension_id = 2

        self.command.associate(line_id, extension_id)
        self.session.post.assert_called_once_with("/lines/1/extensions", {'extension_id': extension_id})

    def test_line_extension_dissociation(self):
        line_id = 1
        extension_id = 2

        self.command.dissociate(line_id, extension_id)
        self.session.delete.assert_called_once_with("/lines/1/extensions/2")


class TestUserVoicemailRelation(TestCommand):

    Command = UserVoicemailRelation

    def test_user_voicemail_association(self):
        user_id = 1
        voicemail_id = 2

        self.command.associate(user_id, voicemail_id)
        self.session.post.assert_called_once_with("/users/1/voicemail", {'voicemail_id': voicemail_id})

    def test_user_voicemail_dissociation(self):
        user_id = 1
        voicemail_id = 2

        self.command.dissociate(user_id, voicemail_id)
        self.session.delete.assert_called_once_with("/users/1/voicemail")


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
