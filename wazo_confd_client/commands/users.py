# Copyright 2014-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import json

from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import (
    UserAgentRelation,
    UserCallPermissionRelation,
    UserEndpointSipRelation,
    UserExternalAppRelation,
    UserFallbackRelation,
    UserForwardRelation,
    UserFuncKeyRelation,
    UserGroupRelation,
    UserLineRelation,
    UserMeBlocklistRelation,
    UserOutgoingCalleridRelation,
    UserScheduleRelation,
    UserServiceRelation,
    UserVoicemailRelation,
)
from wazo_confd_client.util import extract_id, extract_name, url_join


class UserRelation:
    def __init__(self, builder, user_id):
        self.user_id = user_id
        self.user_agent = UserAgentRelation(builder)
        self.user_call_permission = UserCallPermissionRelation(builder)
        self.user_endpoint_sip = UserEndpointSipRelation(builder)
        self.user_external_app = UserExternalAppRelation(builder)
        self.user_fallback = UserFallbackRelation(builder)
        self.user_forward = UserForwardRelation(builder)
        self.user_funckey = UserFuncKeyRelation(builder)
        self.user_group = UserGroupRelation(builder)
        self.user_line = UserLineRelation(builder)
        self.user_outgoing_callerid = UserOutgoingCalleridRelation(builder)
        self.user_schedule = UserScheduleRelation(builder)
        self.user_service = UserServiceRelation(builder)
        self.user_voicemail = UserVoicemailRelation(builder)

    @extract_id
    def add_line(self, line_id):
        return self.user_line.associate(self.user_id, line_id)

    @extract_id
    def remove_line(self, line_id):
        self.user_line.dissociate(self.user_id, line_id)

    def update_lines(self, lines):
        return self.user_line.update_lines(self.user_id, lines)

    def get_endpoint_sip(self, line_id):
        return self.user_endpoint_sip.get_by_user_line(self.user_id, line_id)

    @extract_id
    def add_call_permission(self, call_permission_id):
        return self.user_call_permission.associate(self.user_id, call_permission_id)

    @extract_id
    def remove_call_permission(self, call_permission_id):
        self.user_call_permission.dissociate(self.user_id, call_permission_id)

    @extract_id
    def add_voicemail(self, voicemail_id):
        self.user_voicemail.associate(self.user_id, voicemail_id)

    def remove_voicemail(self):
        self.user_voicemail.dissociate(self.user_id)

    def get_voicemail(self):
        return self.user_voicemail.get_voicemail(self.user_id)

    @extract_id
    def add_agent(self, agent_id):
        self.user_agent.associate(self.user_id, agent_id)

    def remove_agent(self):
        self.user_agent.dissociate(self.user_id)

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

    def update_service(self, service_name, service):
        self.user_service.update_service(self.user_id, service_name, service)

    def get_service(self, service_name):
        return self.user_service.get_service(self.user_id, service_name)

    def list_services(self):
        return self.user_service.list_services(self.user_id)

    def update_services(self, body):
        return self.user_service.update_services(self.user_id, body)

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

    def update_groups(self, groups):
        return self.user_group.associate(self.user_id, groups)

    @extract_id
    def add_schedule(self, schedule_id):
        return self.user_schedule.associate(self.user_id, schedule_id)

    @extract_id
    def remove_schedule(self, schedule_id):
        return self.user_schedule.dissociate(self.user_id, schedule_id)

    def list_external_apps(self, **kwargs):
        return self.user_external_app.list(self.user_id, **kwargs)

    @extract_name(pass_original=True)
    def create_external_app(self, name, body):
        return self.user_external_app.create(self.user_id, name, body)

    @extract_name(pass_original=True)
    def update_external_app(self, name, body):
        self.user_external_app.update(self.user_id, name, body)

    @extract_name()
    def get_external_app(self, name):
        return self.user_external_app.get(self.user_id, name)

    @extract_name()
    def delete_external_app(self, name):
        self.user_external_app.delete(self.user_id, name)

    def list_outgoing_callerids(self):
        return self.user_outgoing_callerid.list(self.user_id)


class UsersCommand(MultiTenantCommand):
    resource = 'users'
    relation_cmd = UserRelation

    def import_csv(self, csvdata, encoding='utf-8', timeout=300, tenant_uuid=None):
        url = url_join(self.resource, "import")
        headers = {'Content-Type': f'text/csv; charset={encoding}'}
        tenant_uuid = tenant_uuid or self._client.tenant_uuid
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        response = self.session.post(
            url, raw=csvdata, check_response=False, timeout=timeout, headers=headers
        )
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            response.raise_for_status()

    def update_csv(self, csvdata, encoding='utf-8', timeout=300):
        url = url_join(self.resource, "import")
        headers = {'Content-Type': f'text/csv; charset={encoding}'}
        response = self.session.put(
            url, raw=csvdata, check_response=False, timeout=timeout, headers=headers
        )
        try:
            return response.json()
        except json.decoder.JSONDecodeError:
            response.raise_for_status()

    def export_csv(self, tenant_uuid=None):
        url = url_join(self.resource, "export")
        headers = {'Accept': 'text/csv; charset=utf-8'}
        tenant_uuid = tenant_uuid or self._client.tenant_uuid
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        response = self.session.get(url, headers=headers)
        return response.content

    def get_main_endpoint_sip(self, user_uuid, view=None):
        url = url_join(self.resource, user_uuid, "lines/main/associated/endpoints/sip")
        params = {}
        if view:
            params['view'] = view
        response = self.session.get(url, params=params)
        return response.json()

    def exist(self, user_uuid):
        url = url_join(self.resource, user_uuid)
        response = self.session.head(url, check_response=False)
        if response.status_code == 404:
            return False
        self.session.check_response(response)
        return True

    @property
    def my_blocklist(self):
        return UserMeBlocklistRelation(self._client)
