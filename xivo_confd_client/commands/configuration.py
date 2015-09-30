# -*- coding: utf-8 -*-

# Copyright (C) 2014-2015 Avencall
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

from xivo_lib_rest_client import HTTPCommand
from xivo_confd_client.util import url_join


class LiveReloadCommand(HTTPCommand):

    def get(self):
        url = url_join('configuration', 'live_reload')
        r = self.session.get(url)

        return r.json()

    def update(self, body):
        url = url_join('configuration', 'live_reload')
        self.session.put(url, body)


class ConfigurationCommand(object):

    def __init__(self, session_builder):
        self.live_reload = LiveReloadCommand(session_builder)
