# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import time
from six.moves import range

from requests import RequestException, HTTPError

from xivo_lib_rest_client import HTTPCommand
from xivo_confd_client.util import url_join


class WaitCommand(HTTPCommand):

    resource = 'infos'

    def __call__(self, retry=20, delay=0.2):
        url = url_join(self.resource)
        for n in range(retry):
            try:
                self.session.get(url, check_response=False)
                return
            except HTTPError as e:
                response = getattr(e, 'response', None)
                if not response:
                    raise
                status_code = getattr(response, 'status_code', None)
                if status_code == '401':
                    return
                raise
            except RequestException:
                if n < retry - 1:
                    time.sleep(delay)
                else:
                    raise
