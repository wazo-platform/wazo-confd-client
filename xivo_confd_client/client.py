# -*- coding: utf-8 -*-

# Copyright (C) 2014 Avencall
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

from requests import Session
from stevedore import extension


class _HTTPCommandProxy(object):

    def __init__(self, host, port, version, Command):
        self.command = Command(host, port, version)

    def __call__(self, *args, **kwargs):
        return self._query_url(self.command)(*args, **kwargs)

    def __getattr__(self, name):
        return self._query_url(getattr(self.command, name))

    def _query_url(self, callable_):
        def decorated(*args, **kwargs):
            session = Session()
            # auth
            # headers
            # ...
            return callable_(session, *args, **kwargs)
        return decorated

    def _build_url(self, url_end):
        return 'http://{host}:{port}/{version}/{url_end}'.format(host=self.host,
                                                                 port=self.port,
                                                                 version=self.version,
                                                                 url_end=url_end)


class Client(object):

    _command_namespace = 'confd_client.commands'

    def __init__(self, host='localhost', port=9487, version='1.1'):
        self._host = host
        self._port = port
        self._version = version
        self._load_plugins()

    def _load_plugins(self):
        extension_manager = extension.ExtensionManager(self._command_namespace)
        extension_manager.map(self._add_command_to_client)

    def _add_command_to_client(self, extension):
        self.__setattr__(extension.name, _HTTPCommandProxy(self._host,
                                                           self._port,
                                                           self._version,
                                                           extension.plugin))
