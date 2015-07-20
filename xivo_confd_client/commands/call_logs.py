# -*- coding: UTF-8 -*-

# Copyright (C) 2015 Avencall
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import requests

from xivo_lib_rest_client import RESTCommand


class CallLogsCommand(RESTCommand):

    DATETIME_FMT = "%Y-%m-%dT%H:%M:%S"

    resource = 'call_logs'

    def list(self, start_date=None, end_date=None):
        params = self.build_params(start_date, end_date)
        response = self.session.get(self.base_url,
                                    params=params,
                                    headers={'Accept': 'text/csv'})

        if response.status_code != requests.codes.ok:
            self.raise_from_response(response)

        return response.text

    def build_params(self, start_date=None, end_date=None):
        params = {}
        if start_date:
            params['start_date'] = start_date.strftime(self.DATETIME_FMT)
        if end_date:
            params['end_date'] = end_date.strftime(self.DATETIME_FMT)
        return params
