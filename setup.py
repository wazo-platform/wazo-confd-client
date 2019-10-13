#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2014-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from setuptools import setup
from setuptools import find_packages

setup(
    name='wazo_confd_client',
    version='1.1.2',  # <confd-api-version>.<confd-client-version>

    description='a simple client library for the wazo-confd HTTP interface',

    author='Wazo Authors',
    author_email='dev@wazo.community',

    url='http://wazo.community',

    packages=find_packages(),

    entry_points={
        'wazo_confd_client.commands': [
            'access_features = wazo_confd_client.commands.access_features:AccessFeaturesCommand',
            'agents = wazo_confd_client.commands.agents:AgentsCommand',
            'agent_skills = wazo_confd_client.commands.skills:SkillsCommand',
            'applications = wazo_confd_client.commands.applications:ApplicationsCommand',
            'call_logs = wazo_confd_client.commands.call_logs:CallLogsCommand',
            'call_filters = wazo_confd_client.commands.call_filters:CallFiltersCommand',
            'call_permissions = wazo_confd_client.commands.call_permissions:CallPermissionsCommand',
            'call_pickups = wazo_confd_client.commands.call_pickups:CallPickupsCommand',
            'confbridge_wazo_default_bridge = wazo_confd_client.commands.confbridge_wazo_default_bridge:ConfBridgeWazoDefaultBridgeCommand',
            'confbridge_wazo_default_user = wazo_confd_client.commands.confbridge_wazo_default_user:ConfBridgeWazoDefaultUserCommand',
            'conferences = wazo_confd_client.commands.conferences:ConferencesCommand',
            'configuration = wazo_confd_client.commands.configuration:ConfigurationCommand',
            'contexts = wazo_confd_client.commands.contexts:ContextsCommand',
            'devices = wazo_confd_client.commands.devices:DevicesCommand',
            'dhcp = wazo_confd_client.commands.dhcp:DHCPCommand',
            'endpoints_custom = wazo_confd_client.commands.endpoints_custom:EndpointsCustomCommand',
            'endpoints_iax = wazo_confd_client.commands.endpoints_iax:EndpointsIAXCommand',
            'endpoints_sccp = wazo_confd_client.commands.endpoints_sccp:EndpointsSccpCommand',
            'endpoints_sip = wazo_confd_client.commands.endpoints_sip:EndpointsSipCommand',
            'entities = wazo_confd_client.commands.entities:EntitiesCommand',
            'extensions = wazo_confd_client.commands.extensions:ExtensionsCommand',
            'extensions_features = wazo_confd_client.commands.extensions_features:ExtensionsFeaturesCommand',
            'features_applicationmap = wazo_confd_client.commands.features_applicationmap:FeaturesApplicationmapCommand',
            'features_featuremap = wazo_confd_client.commands.features_featuremap:FeaturesFeaturemapCommand',
            'features_general = wazo_confd_client.commands.features_general:FeaturesGeneralCommand',
            'funckeys = wazo_confd_client.commands.funckeys:FuncKeysCommand',
            'groups = wazo_confd_client.commands.groups:GroupsCommand',
            'ha = wazo_confd_client.commands.ha:HACommand',
            'hep_general = wazo_confd_client.commands.hep_general:HEPGeneralCommand',
            'iax_callnumberlimits = wazo_confd_client.commands.iax_callnumberlimits:IAXCallNumberLimitsCommand',
            'iax_general = wazo_confd_client.commands.iax_general:IAXGeneralCommand',
            'incalls = wazo_confd_client.commands.incalls:IncallsCommand',
            'infos = wazo_confd_client.commands.infos:InfosCommand',
            'ivr = wazo_confd_client.commands.ivr:IVRCommand',
            'lines = wazo_confd_client.commands.lines:LinesCommand',
            'lines_sip = wazo_confd_client.commands.lines_sip:LinesSIPCommand',
            'outcalls = wazo_confd_client.commands.outcalls:OutcallsCommand',
            'moh = wazo_confd_client.commands.moh:MOHCommand',
            'pagings = wazo_confd_client.commands.pagings:PagingsCommand',
            'parking_lots = wazo_confd_client.commands.parking_lots:ParkingLotsCommand',
            'provisioning_networking = wazo_confd_client.commands.provisioning_networking:ProvisioningNetworkingCommand',
            'queues = wazo_confd_client.commands.queues:QueuesCommand',
            'queues_general = wazo_confd_client.commands.queues_general:QueuesGeneralCommand',
            'queue_skill_rules = wazo_confd_client.commands.skill_rules:SkillRulesCommand',
            'rtp_general = wazo_confd_client.commands.rtp_general:RTPGeneralCommand',
            'rtp_ice_host_candidates = wazo_confd_client.commands.rtp_ice_host_candidates:RTPIceHostCandidatesCommand',
            'registers_iax = wazo_confd_client.commands.registers_iax:RegistersIAXCommand',
            'registers_sip = wazo_confd_client.commands.registers_sip:RegistersSipCommand',
            'registrars = wazo_confd_client.commands.registrars:RegistrarsCommand',
            'sccp_general = wazo_confd_client.commands.sccp_general:SCCPGeneralCommand',
            'schedules = wazo_confd_client.commands.schedules:SchedulesCommand',
            'sip_general = wazo_confd_client.commands.sip_general:SIPGeneralCommand',
            'sounds = wazo_confd_client.commands.sounds:SoundsCommand',
            'sounds_languages = wazo_confd_client.commands.sounds_languages:SoundsLanguagesCommand',
            'switchboards = wazo_confd_client.commands.switchboards:SwitchboardsCommand',
            'timezones = wazo_confd_client.commands.timezones:TimezonesCommand',
            'trunks = wazo_confd_client.commands.trunks:TrunksCommand',
            'unallocated_devices = wazo_confd_client.commands.devices:UnallocatedDevicesCommand',
            'users = wazo_confd_client.commands.users:UsersCommand',
            'voicemails = wazo_confd_client.commands.voicemails:VoicemailsCommand',
            'voicemail_general = wazo_confd_client.commands.voicemail_general:VoicemailGeneralCommand',
            'voicemail_zonemessages = wazo_confd_client.commands.voicemail_zonemessages:VoicemailZoneMessagesCommand',
            'wait_until_ready = wazo_confd_client.commands.wait_until_ready:WaitUntilReadyCommand',
            'wizard = wazo_confd_client.commands.wizard:WizardCommand',
        ],
    }
)
