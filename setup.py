#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2014-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages

setup(
    name='xivo_confd_client',
    version='1.1.2',  # <confd-api-version>.<confd-client-version>

    description='a simple client library for the xivo-confd HTTP interface',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'confd_client.commands': [
            'agents = xivo_confd_client.commands.agents:AgentsCommand',
            'agent_skills = xivo_confd_client.commands.skills:SkillsCommand',
            'applications = xivo_confd_client.commands.applications:ApplicationsCommand',
            'call_logs = xivo_confd_client.commands.call_logs:CallLogsCommand',
            'call_filters = xivo_confd_client.commands.call_filters:CallFiltersCommand',
            'call_permissions = xivo_confd_client.commands.call_permissions:CallPermissionsCommand',
            'call_pickups = xivo_confd_client.commands.call_pickups:CallPickupsCommand',
            'confbridge_wazo_default_bridge = xivo_confd_client.commands.confbridge_wazo_default_bridge:ConfBridgeWazoDefaultBridgeCommand',
            'confbridge_wazo_default_user = xivo_confd_client.commands.confbridge_wazo_default_user:ConfBridgeWazoDefaultUserCommand',
            'conferences = xivo_confd_client.commands.conferences:ConferencesCommand',
            'configuration = xivo_confd_client.commands.configuration:ConfigurationCommand',
            'contexts = xivo_confd_client.commands.contexts:ContextsCommand',
            'devices = xivo_confd_client.commands.devices:DevicesCommand',
            'dhcp = xivo_confd_client.commands.dhcp:DHCPCommand',
            'endpoints_custom = xivo_confd_client.commands.endpoints_custom:EndpointsCustomCommand',
            'endpoints_iax = xivo_confd_client.commands.endpoints_iax:EndpointsIAXCommand',
            'endpoints_sccp = xivo_confd_client.commands.endpoints_sccp:EndpointsSccpCommand',
            'endpoints_sip = xivo_confd_client.commands.endpoints_sip:EndpointsSipCommand',
            'entities = xivo_confd_client.commands.entities:EntitiesCommand',
            'extensions = xivo_confd_client.commands.extensions:ExtensionsCommand',
            'extensions_features = xivo_confd_client.commands.extensions_features:ExtensionsFeaturesCommand',
            'features_applicationmap = xivo_confd_client.commands.features_applicationmap:FeaturesApplicationmapCommand',
            'features_featuremap = xivo_confd_client.commands.features_featuremap:FeaturesFeaturemapCommand',
            'features_general = xivo_confd_client.commands.features_general:FeaturesGeneralCommand',
            'funckeys = xivo_confd_client.commands.funckeys:FuncKeysCommand',
            'groups = xivo_confd_client.commands.groups:GroupsCommand',
            'ha = xivo_confd_client.commands.ha:HACommand',
            'hep_general = xivo_confd_client.commands.hep_general:HEPGeneralCommand',
            'iax_callnumberlimits = xivo_confd_client.commands.iax_callnumberlimits:IAXCallNumberLimitsCommand',
            'iax_general = xivo_confd_client.commands.iax_general:IAXGeneralCommand',
            'incalls = xivo_confd_client.commands.incalls:IncallsCommand',
            'infos = xivo_confd_client.commands.infos:InfosCommand',
            'ivr = xivo_confd_client.commands.ivr:IVRCommand',
            'lines = xivo_confd_client.commands.lines:LinesCommand',
            'lines_sip = xivo_confd_client.commands.lines_sip:LinesSIPCommand',
            'outcalls = xivo_confd_client.commands.outcalls:OutcallsCommand',
            'moh = xivo_confd_client.commands.moh:MOHCommand',
            'pagings = xivo_confd_client.commands.pagings:PagingsCommand',
            'parking_lots = xivo_confd_client.commands.parking_lots:ParkingLotsCommand',
            'provisioning_networking = xivo_confd_client.commands.provisioning_networking:ProvisioningNetworkingCommand',
            'queues = xivo_confd_client.commands.queues:QueuesCommand',
            'queues_general = xivo_confd_client.commands.queues_general:QueuesGeneralCommand',
            'queue_skill_rules = xivo_confd_client.commands.skill_rules:SkillRulesCommand',
            'rtp_general = xivo_confd_client.commands.rtp_general:RTPGeneralCommand',
            'rtp_ice_host_candidates = xivo_confd_client.commands.rtp_ice_host_candidates:RTPIceHostCandidatesCommand',
            'registers_iax = xivo_confd_client.commands.registers_iax:RegistersIAXCommand',
            'registers_sip = xivo_confd_client.commands.registers_sip:RegistersSipCommand',
            'sccp_general = xivo_confd_client.commands.sccp_general:SCCPGeneralCommand',
            'schedules = xivo_confd_client.commands.schedules:SchedulesCommand',
            'sip_general = xivo_confd_client.commands.sip_general:SIPGeneralCommand',
            'sounds = xivo_confd_client.commands.sounds:SoundsCommand',
            'sounds_languages = xivo_confd_client.commands.sounds_languages:SoundsLanguagesCommand',
            'switchboards = xivo_confd_client.commands.switchboards:SwitchboardsCommand',
            'timezones = xivo_confd_client.commands.timezones:TimezonesCommand',
            'trunks = xivo_confd_client.commands.trunks:TrunksCommand',
            'unallocated_devices = xivo_confd_client.commands.devices:UnallocatedDevicesCommand',
            'users = xivo_confd_client.commands.users:UsersCommand',
            'voicemails = xivo_confd_client.commands.voicemails:VoicemailsCommand',
            'voicemail_general = xivo_confd_client.commands.voicemail_general:VoicemailGeneralCommand',
            'voicemail_zonemessages = xivo_confd_client.commands.voicemail_zonemessages:VoicemailZoneMessagesCommand',
            'wait_until_ready = xivo_confd_client.commands.wait_until_ready:WaitUntilReadyCommand',
            'wizard = xivo_confd_client.commands.wizard:WizardCommand',
        ],
    }
)
