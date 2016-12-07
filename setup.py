#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014-2016 The Wazo Authors  (see the AUTHORS file)
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

from setuptools import setup
from setuptools import find_packages

setup(
    name='xivo_confd_client',
    version='1.1.2',  # <confd-api-version>.<confd-client-version>

    description='a simple client library for the xivo-confd HTTP interface',

    author='Avencall',
    author_email='dev@proformatique.com',

    url='https://github.com/wazo-pbx/xivo-confd-client',

    packages=find_packages(),

    entry_points={
        'confd_client.commands': [
            'call_logs = xivo_confd_client.commands.call_logs:CallLogsCommand',
            'call_permissions = xivo_confd_client.commands.call_permissions:CallPermissionsCommand',
            'conferences = xivo_confd_client.commands.conferences:ConferencesCommand',
            'configuration = xivo_confd_client.commands.configuration:ConfigurationCommand',
            'contexts = xivo_confd_client.commands.contexts:ContextsCommand',
            'cti_profiles = xivo_confd_client.commands.cti_profiles:CtiProfilesCommand',
            'devices = xivo_confd_client.commands.devices:DevicesCommand',
            'endpoints_custom = xivo_confd_client.commands.endpoints_custom:EndpointsCustomCommand',
            'endpoints_sccp = xivo_confd_client.commands.endpoints_sccp:EndpointsSccpCommand',
            'endpoints_sip = xivo_confd_client.commands.endpoints_sip:EndpointsSipCommand',
            'entities = xivo_confd_client.commands.entities:EntitiesCommand',
            'extensions = xivo_confd_client.commands.extensions:ExtensionsCommand',
            'funckeys = xivo_confd_client.commands.funckeys:FuncKeysCommand',
            'groups = xivo_confd_client.commands.groups:GroupsCommand',
            'incalls = xivo_confd_client.commands.incalls:IncallsCommand',
            'infos = xivo_confd_client.commands.infos:InfosCommand',
            'ivr = xivo_confd_client.commands.ivr:IVRCommand',
            'lines = xivo_confd_client.commands.lines:LinesCommand',
            'lines_sip = xivo_confd_client.commands.lines_sip:LinesSIPCommand',
            'outcalls = xivo_confd_client.commands.outcalls:OutcallsCommand',
            'queues = xivo_confd_client.commands.queues:QueuesCommand',
            'sip_general = xivo_confd_client.commands.sip_general:SIPGeneralCommand',
            'trunks = xivo_confd_client.commands.trunks:TrunksCommand',
            'users = xivo_confd_client.commands.users:UsersCommand',
            'voicemails = xivo_confd_client.commands.voicemails:VoicemailsCommand',
            'wizard = xivo_confd_client.commands.wizard:WizardCommand',
        ],
    }
)
