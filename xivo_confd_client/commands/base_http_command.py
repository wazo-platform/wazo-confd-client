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


class BaseHTTPCommand(object):

    @property
    def resource(self):
        raise NotImplementedError('The implementation of a command must have a resource field')

    def __init__(self, host, port, version, use_https):
        self.host = host
        self.port = port
        self.version = version
        self.scheme = 'https' if use_https else 'http'
        self.resource_url = self._build_url(self.resource)

    def _build_url(self, url_end):
        return '{scheme}://{host}:{port}/{version}/{url_end}'.format(scheme=self.scheme,
                                                                     host=self.host,
                                                                     port=self.port,
                                                                     version=self.version,
                                                                     url_end=url_end)
