# -*- coding: utf-8 -*-

# Copyright 2014-2017 The Wazo Authors  (see the AUTHORS file)
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
from xivo_confd_client.relations import (UserLineRelation,
                                         UserEndpointSipRelation,
                                         UserVoicemailRelation,
                                         UserFuncKeyRelation,
                                         UserCtiProfileRelation,
                                         UserServiceRelation,
                                         UserForwardRelation,
                                         UserCallPermissionRelation,
                                         UserEntityRelation,
                                         UserFallbackRelation,
                                         UserAgentRelation)
from xivo_confd_client.util import extract_id, url_join


class UserRelation(object):

    def __init__(self, builder, user_id):
        self.user_id = user_id
        self.user_line = UserLineRelation(builder)
        self.user_endpoint_sip = UserEndpointSipRelation(builder)
        self.user_voicemail = UserVoicemailRelation(builder)
        self.user_funckey = UserFuncKeyRelation(builder)
        self.user_cti_profile = UserCtiProfileRelation(builder)
        self.user_service = UserServiceRelation(builder)
        self.user_forward = UserForwardRelation(builder)
        self.user_call_permission = UserCallPermissionRelation(builder)
        self.user_entity = UserEntityRelation(builder)
        self.user_agent = UserAgentRelation(builder)
        self.user_fallback = UserFallbackRelation(builder)

    @extract_id
    def add_line(self, line_id):
        return self.user_line.associate(self.user_id, line_id)

    @extract_id
    def remove_line(self, line_id):
        self.user_line.dissociate(self.user_id, line_id)

    def list_lines(self):
        return self.user_line.list_by_user(self.user_id)

    def get_endpoint_sip(self, line_id):
        return self.user_endpoint_sip.get_by_user_line(self.user_id, line_id)

    @extract_id
    def add_call_permission(self, call_permission_id):
        return self.user_call_permission.associate(self.user_id, call_permission_id)

    @extract_id
    def remove_call_permission(self, call_permission_id):
        self.user_call_permission.dissociate(self.user_id, call_permission_id)

    def list_call_permissions(self):
        return self.user_call_permission.list_by_user(self.user_id)

    @extract_id
    def add_entity(self, entity_id):
        return self.user_entity.associate(self.user_id, entity_id)

    def get_entity(self):
        return self.user_entity.get_by_user(self.user_id)

    @extract_id
    def add_voicemail(self, voicemail_id):
        self.user_voicemail.associate(self.user_id, voicemail_id)

    def remove_voicemail(self):
        self.user_voicemail.dissociate(self.user_id)

    def get_voicemail(self):
        return self.user_voicemail.get_by_user(self.user_id)

    @extract_id
    def add_agent(self, agent_id):
        self.user_agent.associate(self.user_id, agent_id)

    def remove_agent(self):
        self.user_agent.dissociate(self.user_id)

    def get_agent(self):
        return self.user_agent.get_by_user(self.user_id)

    def add_funckey(self, position, funckey):
        self.update_funckey(position, funckey)

    def update_funckey(self, position, funckey):
        self.user_funckey.update_funckey(self.user_id, position, funckey)

    def remove_funckey(self, position):
        self.user_funckey.remove_funckey(self.user_id, position)

    def get_funckey(self, position):
        return self.user_funckey.get_funckey(self.user_id, position)

    def list_funckeys(self):
        return self.user_funckey.list_funckeys(self.user_id)

    def update_funckeys(self, funckeys):
        self.user_funckey.update_funckeys(self.user_id, funckeys)

    @extract_id
    def add_funckey_template(self, template_id):
        self.user_funckey.associate_funckey_template(self.user_id, template_id)

    @extract_id
    def remove_funckey_template(self, template_id):
        self.user_funckey.dissociate_funckey_template(self.user_id, template_id)

    def get_cti_profile(self):
        return self.user_cti_profile.get_by_user(self.user_id)

    @extract_id
    def add_cti_profile(self, profile_id):
        self.user_cti_profile.associate(self.user_id, profile_id)

    def disable_cti_profile(self):
        self.user_cti_profile.disable(self.user_id)

    def update_cti_profile(self, cti_profile):
        self.user_cti_profile.update(self.user_id, cti_profile)

    def update_service(self, service_name, service):
        self.user_service.update_service(self.user_id, service_name, service)

    def get_service(self, service_name):
        return self.user_service.get_service(self.user_id, service_name)

    def list_services(self):
        return self.user_service.list_services(self.user_id)

    def update_forward(self, forward_name, forward):
        self.user_forward.update_forward(self.user_id, forward_name, forward)

    def get_forward(self, forward_name):
        return self.user_forward.get_forward(self.user_id, forward_name)

    def list_forwards(self):
        return self.user_forward.list_forwards(self.user_id)

    def update_forwards(self, body):
        return self.user_forward.update_forwards(self.user_id, body)

    def update_fallbacks(self, fallbacks):
        self.user_fallback.update_fallbacks(self.user_id, fallbacks)

    def list_fallbacks(self):
        return self.user_fallback.list_fallbacks(self.user_id)


class UsersCommand(CRUDCommand):

    resource = 'users'
    relation_cmd = UserRelation

    def import_csv(self, csvdata, encoding='utf-8', timeout=300):
        url = url_join(self.resource, "import")
        headers = {'Content-Type': 'text/csv; charset={}'.format(encoding)}
        response = self.session.post(url,
                                     raw=csvdata,
                                     check_response=False,
                                     timeout=timeout,
                                     headers=headers)
        return response.json()

    def update_csv(self, csvdata, encoding='utf-8', timeout=300):
        url = url_join(self.resource, "import")
        headers = {'Content-Type': 'text/csv; charset={}'.format(encoding)}
        response = self.session.put(url,
                                    raw=csvdata,
                                    check_response=False,
                                    timeout=timeout,
                                    headers=headers)
        return response.json()

    def export_csv(self):
        url = url_join(self.resource, "export")
        headers = {'Accept': 'text/csv; charset=utf-8'}
        response = self.session.get(url, headers=headers)
        return response.content

    def get_main_endpoint_sip(self, user_uuid):
        url = url_join(self.resource, user_uuid, "lines/main/associated/endpoints/sip")
        response = self.session.get(url)
        return response.json()
