# -*- coding: UTF-8 -*-
# Copyright 2015-2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import HTTPCommand
from xivo_confd_client.util import url_join


class UserLineRelation(HTTPCommand):

    def associate(self, user_id, line_id):
        url = url_join('users', user_id, 'lines', line_id)
        self.session.put(url)

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

    def update_lines(self, user_id, lines):
        url = url_join('users', user_id, 'lines')
        body = {'lines': [{'id': line['id']} for line in lines]}
        self.session.put(url, body)


class UserEndpointSipRelation(HTTPCommand):

    def get_by_user_line(self, user_uuid, line_id):
        url = url_join('users', user_uuid, 'lines', line_id, 'associated', 'endpoints', 'sip')
        response = self.session.get(url)
        return response.json()


class UserVoicemailRelation(HTTPCommand):

    def associate(self, user_id, voicemail_id):
        url = url_join('users', user_id, 'voicemails', voicemail_id)
        self.session.put(url)

    def dissociate(self, user_id):
        url = url_join('users', user_id, 'voicemails')
        self.session.delete(url)

    def get_by_user(self, user_id):
        url = url_join('users', user_id, 'voicemails')
        response = self.session.get(url)
        return response.json()

    def list_by_voicemail(self, voicemail_id):
        url = url_join('voicemails', voicemail_id, 'users')
        response = self.session.get(url)
        return response.json()


class UserAgentRelation(HTTPCommand):

    def associate(self, user_id, agent_id):
        url = url_join('users', user_id, 'agents', agent_id)
        self.session.put(url)

    def dissociate(self, user_id):
        url = url_join('users', user_id, 'agents')
        self.session.delete(url)

    def get_by_user(self, user_id):
        url = url_join('users', user_id, 'agents')
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
        url = url_join('lines', line_id, 'extensions', extension_id)
        self.session.put(url)

    def dissociate(self, line_id, extension_id):
        url = url_join('lines', line_id, 'extensions', extension_id)
        self.session.delete(url)

    def list_by_line(self, line_id):
        url = url_join('lines', line_id, 'extensions')
        response = self.session.get(url)
        return response.json()

    def list_by_extension(self, extension_id):
        url = url_join('extensions', extension_id, 'lines')
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

    def update_funckeys(self, user_id, funckeys):
        url = url_join('users', user_id, 'funckeys')
        self.session.put(url, funckeys)

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

    def update(self, user_id, cti_profile):
        url = url_join('users', user_id, 'cti')
        body = {'cti_profile_id': cti_profile.get('id'),
                'enabled': True if cti_profile.get('id') is not None else False}
        self.session.put(url, body)

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

    def list_by_user(self, user_id):
        url = url_join('users', user_id, 'callpermissions')
        response = self.session.get(url)
        return response.json()

    def list_by_call_permission(self, call_permission_id):
        url = url_join('callpermissions', call_permission_id, 'users')
        response = self.session.get(url)
        return response.json()


class UserEntityRelation(HTTPCommand):

    def associate(self, user_id, entity_id):
        url = url_join('users', user_id, 'entities', entity_id)
        self.session.put(url)

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

    def get_by_trunk(self, trunk_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'sip')
        response = self.session.get(url)
        return response.json()

    def get_by_endpoint_sip(self, sip_id):
        url = url_join('endpoints', 'sip', sip_id, 'trunks')
        response = self.session.get(url)
        return response.json()


class TrunkEndpointCustomRelation(HTTPCommand):

    def associate(self, trunk_id, custom_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'custom', custom_id)
        self.session.put(url)

    def dissociate(self, trunk_id, custom_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'custom', custom_id)
        self.session.delete(url)

    def get_by_trunk(self, trunk_id):
        url = url_join('trunks', trunk_id, 'endpoints', 'custom')
        response = self.session.get(url)
        return response.json()

    def get_by_endpoint_custom(self, custom_id):
        url = url_join('endpoints', 'custom', custom_id, 'trunks')
        response = self.session.get(url)
        return response.json()


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
            result = {'exten': extension['exten'],
                      'context': extension['context']}
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
