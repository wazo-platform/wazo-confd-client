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

import json

from .exceptions import UnexpectedResultError
from xivo_lib_rest_client import BaseHTTPCommand


class InfosCommand(BaseHTTPCommand):

    resource = 'infos'

    def __call__(self):
        return self.get()

    def get(self):
        r = self.session.get(self.resource_url)
        if r.status_code != 200:
            raise UnexpectedResultError()

        return json.loads(r.content)