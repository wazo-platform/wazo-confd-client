# Copyright 2015-2025 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later
from __future__ import annotations

from wazo_lib_rest_client import HTTPCommand
from wazo_lib_rest_client.client import BaseClient

from wazo_confd_client.util import url_join


class UserLineRelation(HTTPCommand):
    def associate(self, user_id, line_id):
        url = url_join('users', user_id, 'lines', line_id)
        self.session.put(url)

    def dissociate(self, user_id, line_id):
        url = url_join('users', user_id, 'lines', line_id)
        self.session.delete(url)

    def update_lines(self, user_id, lines):
        url = url_join('users', user_id, 'lines')
        body = {'lines': [{'id': line['id']} for line in lines]}
        self.session.put(url, body)


class UserEndpointSipRelation(HTTPCommand):
    def get_by_user_line(self, user_uuid, line_id, view=None):
        url = url_join(
            'users', user_uuid, 'lines', line_id, 'associated', 'endpoints', 'sip'
        )
        params = {}
        if view:
            params['view'] = view
        response = self.session.get(url, params=params)
        return response.json()


class UserVoicemailRelation(HTTPCommand):
    def associate(self, user_id, voicemail_id):
        url = url_join('users', user_id, 'voicemails', voicemail_id)
        self.session.put(url)

    def dissociate(self, user_id):
        url = url_join('users', user_id, 'voicemails')
        self.session.delete(url)

    def list_users(self, voicemail_id):
        url = url_join('voicemails', voicemail_id)
        response = self.session.get(url)
        return response.json()['users']

    def get_voicemail(self, user_id):
        url = url_join('users', user_id, 'voicemails')
        response = self.session.get(url)
        voicemails = response.json()['items']
        return voicemails[0] if voicemails else None


class UserAgentRelation(HTTPCommand):
    def associate(self, user_id, agent_id):
        url = url_join('users', user_id, 'agents', agent_id)
        self.session.put(url)

    def dissociate(self, user_id):
        url = url_join('users', user_id, 'agents')
        self.session.delete(url)


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


class LineApplicationRelation(HTTPCommand):
    def associate(self, line_id, application_uuid):
        url = url_join('lines', line_id, 'applications', application_uuid)
        self.session.put(url)

    def dissociate(self, line_id, application_uuid):
        url = url_join('lines', line_id, 'applications', application_uuid)
        self.session.delete(url)


class LineExtensionRelation(HTTPCommand):
    def associate(self, line_id, extension_id):
        url = url_join('lines', line_id, 'extensions', extension_id)
        self.session.put(url)

    def dissociate(self, line_id, extension_id):
        url = url_join('lines', line_id, 'extensions', extension_id)
        self.session.delete(url)


class LineEndpointSipRelation(HTTPCommand):
    def associate(self, line_id, sip_id):
        url = url_join('lines', line_id, 'endpoints', 'sip', sip_id)
        self.session.put(url)

    def dissociate(self, line_id, sip_id):
        url = url_join('lines', line_id, 'endpoints', 'sip', sip_id)
        self.session.delete(url)


class LineEndpointSccpRelation(HTTPCommand):
    def associate(self, line_id, sccp_id):
        url = url_join('lines', line_id, 'endpoints', 'sccp', sccp_id)
        self.session.put(url)

    def dissociate(self, line_id, sccp_id):
        url = url_join('lines', line_id, 'endpoints', 'sccp', sccp_id)
        self.session.delete(url)


class LineEndpointCustomRelation(HTTPCommand):
    def associate(self, line_id, custom_id):
        url = url_join('lines', line_id, 'endpoints', 'custom', custom_id)
        self.session.put(url)

    def dissociate(self, line_id, custom_id):
        url = url_join('lines', line_id, 'endpoints', 'custom', custom_id)
        self.session.delete(url)


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

    def update_funckeys(self, user_id, funckeys):
        url = url_join('users', user_id, 'funckeys')
        self.session.put(url, funckeys)

    def associate_funckey_template(self, user_id, template_id):
        url = url_join('users', user_id, 'funckeys', 'templates', template_id)
        self.session.put(url)

    def dissociate_funckey_template(self, user_id, template_id):
        url = url_join('users', user_id, 'funckeys', 'templates', template_id)
        self.session.delete(url)


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

    def update_services(self, user_id, services):
        url = url_join('users', user_id, 'services')
        self.session.put(url, services)


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


class UserEntityRelation(HTTPCommand):
    def get_by_user(self, user_id):
        url = url_join('users', user_id, 'entities')
        response = self.session.get(url)
        return response.json()


class TrunkEndpointSipRelation(HTTPCommand):
    def associate(self, trunk_id, sip_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'sip', sip_id)
        self.session.put(url)

    def dissociate(self, trunk_id, sip_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'sip', sip_id)
        self.session.delete(url)


class TrunkEndpointIAXRelation(HTTPCommand):
    def associate(self, trunk_id, iax_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'iax', iax_id)
        self.session.put(url)

    def dissociate(self, trunk_id, iax_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'iax', iax_id)
        self.session.delete(url)


class TrunkRegisterSipRelation(HTTPCommand):
    def associate(self, trunk_id, sip_id):
        url = url_join('trunks', trunk_id, 'registers', 'sip', sip_id)
        self.session.put(url)

    def dissociate(self, trunk_id, sip_id):
        url = url_join('trunks', trunk_id, 'registers', 'sip', sip_id)
        self.session.delete(url)


class TrunkRegisterIAXRelation(HTTPCommand):
    def associate(self, trunk_id, iax_id):
        url = url_join('trunks', trunk_id, 'registers', 'iax', iax_id)
        self.session.put(url)

    def dissociate(self, trunk_id, iax_id):
        url = url_join('trunks', trunk_id, 'registers', 'iax', iax_id)
        self.session.delete(url)


class TrunkEndpointCustomRelation(HTTPCommand):
    def associate(self, trunk_id, custom_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'custom', custom_id)
        self.session.put(url)

    def dissociate(self, trunk_id, custom_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'custom', custom_id)
        self.session.delete(url)


class IncallExtensionRelation(HTTPCommand):
    def associate(self, incall_id, extension_id):
        url = url_join('incalls', incall_id, 'extensions', extension_id)
        self.session.put(url)

    def dissociate(self, incall_id, extension_id):
        url = url_join('incalls', incall_id, 'extensions', extension_id)
        self.session.delete(url)


class OutcallTrunkRelation(HTTPCommand):
    def associate(self, outcall_id, trunks):
        url = url_join('outcalls', outcall_id, 'trunks')
        body = {'trunks': [{'id': trunk['id']} for trunk in trunks]}
        self.session.put(url, body)


class OutcallExtensionRelation(HTTPCommand):
    def associate(self, outcall_id, extension_id, **body):
        url = url_join('outcalls', outcall_id, 'extensions', extension_id)
        self.session.put(url, body)

    def dissociate(self, outcall_id, extension_id):
        url = url_join('outcalls', outcall_id, 'extensions', extension_id)
        self.session.delete(url)


class GroupExtensionRelation(HTTPCommand):
    def associate(self, group_id, extension_id):
        url = url_join('groups', group_id, 'extensions', extension_id)
        self.session.put(url)

    def dissociate(self, group_id, extension_id):
        url = url_join('groups', group_id, 'extensions', extension_id)
        self.session.delete(url)


class GroupMemberUserRelation(HTTPCommand):
    def associate(self, group_id, users):
        url = url_join('groups', group_id, 'members', 'users')
        body = {'users': []}
        for user in users:
            result = {'uuid': user['uuid']}
            if 'priority' in user:
                result['priority'] = user['priority']
            body['users'].append(result)
        self.session.put(url, body)


class GroupMemberExtensionRelation(HTTPCommand):
    def associate(self, group_id, extensions):
        url = url_join('groups', group_id, 'members', 'extensions')
        body = {'extensions': []}
        for extension in extensions:
            result = {'exten': extension['exten'], 'context': extension['context']}
            if 'priority' in extension:
                result['priority'] = extension['priority']
            body['extensions'].append(result)
        self.session.put(url, body)


class UserGroupRelation(HTTPCommand):
    def associate(self, user_id, groups):
        url = url_join('users', user_id, 'groups')
        body = {'groups': [{'id': group['id']} for group in groups]}
        self.session.put(url, body)


class GroupFallbackRelation(HTTPCommand):
    def list_fallbacks(self, group_id):
        url = url_join('groups', group_id, 'fallbacks')
        response = self.session.get(url)
        return response.json()

    def update_fallbacks(self, group_id, fallbacks):
        url = url_join('groups', group_id, 'fallbacks')
        self.session.put(url, fallbacks)


class UserFallbackRelation(HTTPCommand):
    def list_fallbacks(self, user_id):
        url = url_join('users', user_id, 'fallbacks')
        response = self.session.get(url)
        return response.json()

    def update_fallbacks(self, user_id, fallbacks):
        url = url_join('users', user_id, 'fallbacks')
        self.session.put(url, fallbacks)


class ConferenceExtensionRelation(HTTPCommand):
    def associate(self, conference_id, extension_id):
        url = url_join('conferences', conference_id, 'extensions', extension_id)
        self.session.put(url)

    def dissociate(self, conference_id, extension_id):
        url = url_join('conferences', conference_id, 'extensions', extension_id)
        self.session.delete(url)


class ParkingLotExtensionRelation(HTTPCommand):
    def associate(self, parking_lot_id, extension_id):
        url = url_join('parkinglots', parking_lot_id, 'extensions', extension_id)
        self.session.put(url)

    def dissociate(self, parking_lot_id, extension_id):
        url = url_join('parkinglots', parking_lot_id, 'extensions', extension_id)
        self.session.delete(url)


class PagingMemberUserRelation(HTTPCommand):
    def associate(self, paging_id, users):
        url = url_join('pagings', paging_id, 'members', 'users')
        body = {'users': [{'uuid': user['uuid']} for user in users]}
        self.session.put(url, body)


class PagingCallerUserRelation(HTTPCommand):
    def associate(self, paging_id, users):
        url = url_join('pagings', paging_id, 'callers', 'users')
        body = {'users': [{'uuid': user['uuid']} for user in users]}
        self.session.put(url, body)


class SwitchboardMemberUserRelation(HTTPCommand):
    def associate(self, switchboard_id, users):
        url = url_join('switchboards', switchboard_id, 'members', 'users')
        body = {'users': [{'uuid': user['uuid']} for user in users]}
        self.session.put(url, body)


class SwitchboardFallbackRelation(HTTPCommand):
    def list_fallbacks(self, switchboard_id):
        url = url_join('switchboards', switchboard_id, 'fallbacks')
        response = self.session.get(url)
        return response.json()

    def update_fallbacks(self, switchboard_id, fallbacks):
        url = url_join('switchboards', switchboard_id, 'fallbacks')
        self.session.put(url, fallbacks)


class IncallScheduleRelation(HTTPCommand):
    def associate(self, incall_id, schedule_id):
        url = url_join('incalls', incall_id, 'schedules', schedule_id)
        self.session.put(url)

    def dissociate(self, incall_id, schedule_id):
        url = url_join('incalls', incall_id, 'schedules', schedule_id)
        self.session.delete(url)


class UserScheduleRelation(HTTPCommand):
    def associate(self, user_id, schedule_id):
        url = url_join('users', user_id, 'schedules', schedule_id)
        self.session.put(url)

    def dissociate(self, user_id, schedule_id):
        url = url_join('users', user_id, 'schedules', schedule_id)
        self.session.delete(url)


class GroupScheduleRelation(HTTPCommand):
    def associate(self, group_id, schedule_id):
        url = url_join('groups', group_id, 'schedules', schedule_id)
        self.session.put(url)

    def dissociate(self, group_id, schedule_id):
        url = url_join('groups', group_id, 'schedules', schedule_id)
        self.session.delete(url)


class QueueScheduleRelation(HTTPCommand):
    def associate(self, queue_id, schedule_id):
        url = url_join('queues', queue_id, 'schedules', schedule_id)
        self.session.put(url)

    def dissociate(self, queue_id, schedule_id):
        url = url_join('queues', queue_id, 'schedules', schedule_id)
        self.session.delete(url)


class OutcallScheduleRelation(HTTPCommand):
    def associate(self, outcall_id, schedule_id):
        url = url_join('outcalls', outcall_id, 'schedules', schedule_id)
        self.session.put(url)

    def dissociate(self, outcall_id, schedule_id):
        url = url_join('outcalls', outcall_id, 'schedules', schedule_id)
        self.session.delete(url)


class OutcallCallPermissionRelation(HTTPCommand):
    def associate(self, outcall_id, call_permission_id):
        url = url_join('outcalls', outcall_id, 'callpermissions', call_permission_id)
        self.session.put(url)

    def dissociate(self, outcall_id, call_permission_id):
        url = url_join('outcalls', outcall_id, 'callpermissions', call_permission_id)
        self.session.delete(url)


class GroupCallPermissionRelation(HTTPCommand):
    def associate(self, group_id, call_permission_id):
        url = url_join('groups', group_id, 'callpermissions', call_permission_id)
        self.session.put(url)

    def dissociate(self, group_id, call_permission_id):
        url = url_join('groups', group_id, 'callpermissions', call_permission_id)
        self.session.delete(url)


class CallFilterRecipientUserRelation(HTTPCommand):
    def associate(self, call_filter_id, users):
        url = url_join('callfilters', call_filter_id, 'recipients', 'users')
        body = {'users': []}
        for user in users:
            result = {'uuid': user['uuid']}
            if user.get('timeout'):
                result['timeout'] = user['timeout']
            body['users'].append(result)
        self.session.put(url, body)


class CallFilterSurrogateUserRelation(HTTPCommand):
    def associate(self, call_filter_id, users):
        url = url_join('callfilters', call_filter_id, 'surrogates', 'users')
        body = {'users': [{'uuid': user['uuid']} for user in users]}
        self.session.put(url, body)


class CallFilterFallbackRelation(HTTPCommand):
    def update_fallbacks(self, call_filter_id, fallbacks):
        url = url_join('callfilters', call_filter_id, 'fallbacks')
        self.session.put(url, fallbacks)


class CallPickupInterceptorUserRelation(HTTPCommand):
    def associate(self, call_pickup_id, users):
        url = url_join('callpickups', call_pickup_id, 'interceptors', 'users')
        body = {'users': [{'uuid': user['uuid']} for user in users]}
        self.session.put(url, body)


class CallPickupTargetUserRelation(HTTPCommand):
    def associate(self, call_pickup_id, users):
        url = url_join('callpickups', call_pickup_id, 'targets', 'users')
        body = {'users': [{'uuid': user['uuid']} for user in users]}
        self.session.put(url, body)


class CallPickupInterceptorGroupRelation(HTTPCommand):
    def associate(self, call_pickup_id, groups):
        url = url_join('callpickups', call_pickup_id, 'interceptors', 'groups')
        body = {'groups': [{'id': group['id']} for group in groups]}
        self.session.put(url, body)


class CallPickupTargetGroupRelation(HTTPCommand):
    def associate(self, call_pickup_id, groups):
        url = url_join('callpickups', call_pickup_id, 'targets', 'groups')
        body = {'groups': [{'id': group['id']} for group in groups]}
        self.session.put(url, body)


class QueueFallbackRelation(HTTPCommand):
    def list_fallbacks(self, queue_id):
        url = url_join('queues', queue_id, 'fallbacks')
        response = self.session.get(url)
        return response.json()

    def update_fallbacks(self, queue_id, fallbacks):
        url = url_join('queues', queue_id, 'fallbacks')
        self.session.put(url, fallbacks)


class QueueExtensionRelation(HTTPCommand):
    def associate(self, queue_id, extension_id):
        url = url_join('queues', queue_id, 'extensions', extension_id)
        self.session.put(url)

    def dissociate(self, queue_id, extension_id):
        url = url_join('queues', queue_id, 'extensions', extension_id)
        self.session.delete(url)


class ContextContextRelation(HTTPCommand):
    def associate(self, context_id, contexts):
        url = url_join('contexts', context_id, 'contexts')
        body = {'contexts': [{'id': context['id']} for context in contexts]}
        self.session.put(url, body)


class ContextRangeRelation(HTTPCommand):
    def list_ranges(self, context_id, range_type, tenant_uuid=None, **kwargs):
        headers = dict(self.session.READ_HEADERS)
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = url_join('contexts', context_id, 'ranges', range_type)
        response = self.session.get(url, headers=headers, params=kwargs)
        return response.json()


class QueueMemberAgentRelation(HTTPCommand):
    def associate(self, queue_id, agent_id, **kwargs):
        url = url_join('queues', queue_id, 'members', 'agents', agent_id)
        self.session.put(url, kwargs)

    def dissociate(self, queue_id, agent_id):
        url = url_join('queues', queue_id, 'members', 'agents', agent_id)
        self.session.delete(url)


class QueueMemberUserRelation(HTTPCommand):
    def associate(self, queue_id, user_uuid, **kwargs):
        url = url_join('queues', queue_id, 'members', 'users', user_uuid)
        self.session.put(url, kwargs)

    def dissociate(self, queue_id, user_uuid):
        url = url_join('queues', queue_id, 'members', 'users', user_uuid)
        self.session.delete(url)


class AgentSkillRelation(HTTPCommand):
    def associate(self, agent_id, skill_id, **kwargs):
        weight = kwargs.pop('weight', None)
        if weight is not None:
            kwargs['skill_weight'] = weight

        url = url_join('agents', agent_id, 'skills', skill_id)
        self.session.put(url, kwargs)

    def dissociate(self, agent_id, skill_id):
        url = url_join('agents', agent_id, 'skills', skill_id)
        self.session.delete(url)


class UserExternalAppRelation(HTTPCommand):
    def list(self, user_uuid, **kwargs):
        url = url_join('users', user_uuid, 'external', 'apps')
        response = self.session.get(url, params=kwargs)
        return response.json()

    def create(self, user_uuid, name, body):
        url = url_join('users', user_uuid, 'external', 'apps', name)
        response = self.session.post(url, body)
        return response.json()

    def update(self, user_uuid, name, body):
        url = url_join('users', user_uuid, 'external', 'apps', name)
        self.session.put(url, body)

    def get(self, user_uuid, name):
        url = url_join('users', user_uuid, 'external', 'apps', name)
        response = self.session.get(url)
        return response.json()

    def delete(self, user_uuid, name):
        url = url_join('users', user_uuid, 'external', 'apps', name)
        self.session.delete(url)


class UserOutgoingCalleridRelation(HTTPCommand):
    def list(self, user_uuid, tenant_uuid=None, **kwargs):
        headers = dict(self.session.READ_HEADERS)
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid

        url = url_join('users', user_uuid, 'callerids', 'outgoing')
        response = self.session.get(url, headers=headers, params=kwargs)
        return response.json()


class UserMeBlocklistNumberRelation(HTTPCommand):
    resource = 'users/me/blocklist/numbers'

    def __init__(self, client: BaseClient, number_uuid: str) -> None:
        super().__init__(client)
        self.number_uuid = number_uuid

    def update(self, number: dict):
        url = url_join(self.resource, self.number_uuid)
        self.session.put(url, json=number)

    def delete(self):
        url = url_join(self.resource, self.number_uuid)
        self.session.delete(url)

    def get(self):
        url = url_join(self.resource, self.number_uuid)
        response = self.session.get(url)
        return response.json()


class UserMeBlocklistNumbersRelation(HTTPCommand):
    resource = 'users/me/blocklist/numbers'

    def __init__(self, client: BaseClient) -> None:
        super().__init__(client)

    def list(self, **kwargs):
        url = url_join(self.resource)
        response = self.session.get(url, params=kwargs)
        return response.json()

    def create(self, number: dict):
        url = url_join(self.resource)
        response = self.session.post(url, json=number)
        return response.json()

    def __call__(self, number_uuid: str) -> UserMeBlocklistNumberRelation:
        return UserMeBlocklistNumberRelation(self._client, number_uuid)


class UserMeBlocklistRelation(HTTPCommand):
    def __init__(self, client: BaseClient) -> None:
        super().__init__(client)

    @property
    def numbers(self) -> UserMeBlocklistNumbersRelation:
        return UserMeBlocklistNumbersRelation(self._client)


class UserBlocklistNumbersRelation(HTTPCommand):
    resource = 'users/{user_id}/blocklist/numbers'

    def __init__(self, client: BaseClient, user_id: str | int) -> None:
        super().__init__(client)
        self.user_id = user_id

    def lookup(self, tenant_uuid: str | None = None, **kwargs):
        url = url_join(self.resource.format(user_id=self.user_id))
        headers = {}
        if tenant_uuid:
            headers['Wazo-Tenant'] = tenant_uuid
        response = self.session.head(
            url, headers=headers, params=kwargs, check_response=False
        )
        if response.status_code == 404:
            return None
        else:
            self.session.check_response(response)
            number_uuid = response.headers['Wazo-Blocklist-Number-UUID']
            return number_uuid


class UserBlocklistRelation(HTTPCommand):
    resource = 'users/{user_id}/blocklist'

    def __init__(self, client: BaseClient, user_id: str | int) -> None:
        super().__init__(client)
        self.user_id = user_id

    @property
    def numbers(self) -> UserBlocklistNumbersRelation:
        return UserBlocklistNumbersRelation(self._client, self.user_id)
