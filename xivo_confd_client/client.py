# -*- coding: utf-8 -*-
# Copyright (C) 2015 Avencall
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

import requests

from xivo_lib_rest_client.client import BaseClient
from xivo_confd_client.session import ConfdSession


class ConfdClient(BaseClient):

    namespace = 'confd_client.commands'

    def __init__(self,
                 host,
                 port=9486,
                 version='1.1',
                 username=None,
                 password=None,
                 **kwargs):
        super(ConfdClient, self).__init__(
            host=host,
            port=port,
            version=version,
            **kwargs)
        self.username = username
        self.password = password

    def session(self):
        session = super(ConfdClient, self).session()
        if self.username and self.password:
            session.auth = requests.auth.HTTPDigestAuth(self.username, self.password)
        return ConfdSession(session, self.url())
