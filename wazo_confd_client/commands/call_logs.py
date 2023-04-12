# Copyright 2015-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import requests

from wazo_lib_rest_client import RESTCommand


class CallLogsCommand(RESTCommand):
    DATETIME_FMT = "%Y-%m-%dT%H:%M:%S"

    resource = 'call_logs'

    def list(self, start_date=None, end_date=None):
        params = self.build_params(start_date, end_date)
        response = self.session.get(
            self.resource, params=params, headers={'Accept': 'text/csv'}
        )

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
