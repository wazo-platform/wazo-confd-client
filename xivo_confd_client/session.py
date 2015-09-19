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
import json


class ConfdSession(object):

    OK_STATUSES = (requests.codes.ok,
                   requests.codes.created,
                   requests.codes.no_content)

    READ_HEADERS = {'Accept': 'application/json'}

    WRITE_HEADERS = {'Accept': 'application/json',
                     'Content-Type': 'application/json'}

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def check_response(self, response):
        if response.status_code not in self.OK_STATUSES:
            try:
                messages = response.json()
                response.reason = ". ".join(messages)
            finally:
                response.raise_for_status()

    def clean_url(self, part):
        return "{}/{}".format(self.base_url.rstrip('/'), part.lstrip('/'))

    def get(self, url, **kwargs):
        kwargs.setdefault('headers', self.READ_HEADERS)
        url = self.clean_url(url)
        response = self.session.get(url, **kwargs)
        self.check_response(response)
        return response

    def post(self, url, body, **kwargs):
        kwargs.setdefault('headers', self.WRITE_HEADERS)
        url = self.clean_url(url)
        encoded_body = json.dumps(body)
        response = self.session.post(url, data=encoded_body, **kwargs)
        self.check_response(response)
        return response

    def put(self, url, body, **kwargs):
        kwargs.setdefault('headers', self.WRITE_HEADERS)
        url = self.clean_url(url)
        encoded_body = json.dumps(body)
        response = self.session.put(url, data=encoded_body, **kwargs)
        self.check_response(response)
        return response

    def delete(self, url, **kwargs):
        kwargs.setdefault('headers', self.READ_HEADERS)
        url = self.clean_url(url)
        response = self.session.delete(url, **kwargs)
        self.check_response(response)
        return response
