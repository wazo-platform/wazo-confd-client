# Copyright 2018-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client import RESTCommand


class RTPIceHostCandidatesCommand(RESTCommand):
    resource = 'asterisk/rtp/ice_host_candidates'

    def get(self):
        response = self.session.get(self.resource)
        return response.json()

    def update(self, body):
        self.session.put(self.resource, body)
