# Copyright 2015-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import json
import requests


class ConfdSession:

    OK_STATUSES = (requests.codes.ok, requests.codes.created, requests.codes.no_content)

    READ_HEADERS = {'Accept': 'application/json'}

    WRITE_HEADERS = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def check_response(self, response, check=True):
        if not check:
            return

        if response.status_code not in self.OK_STATUSES:
            try:
                messages = response.json()
            except ValueError:
                pass
            else:
                response.reason = ". ".join(messages)

            response.raise_for_status()

    def clean_url(self, part):
        return f"{self.base_url.rstrip('/')}/{part.lstrip('/')}"

    def head(self, url, **kwargs):
        kwargs.setdefault('headers', self.READ_HEADERS)
        check_response = kwargs.pop('check_response', True)

        url = self.clean_url(url)
        response = self.session.head(url, **kwargs)

        self.check_response(response, check_response)
        return response

    def get(self, url, **kwargs):
        kwargs.setdefault('headers', self.READ_HEADERS)
        check_response = kwargs.pop('check_response', True)

        url = self.clean_url(url)
        response = self.session.get(url, **kwargs)

        self.check_response(response, check_response)
        return response

    def post(self, url, body=None, **kwargs):
        kwargs.setdefault('headers', self.WRITE_HEADERS)
        check_response = kwargs.pop('check_response', True)

        url = self.clean_url(url)
        encoded_body = self.encode_body(body, kwargs)
        response = self.session.post(url, data=encoded_body, **kwargs)

        self.check_response(response, check_response)
        return response

    def put(self, url, body=None, **kwargs):
        kwargs.setdefault('headers', self.WRITE_HEADERS)
        check_response = kwargs.pop('check_response', True)

        url = self.clean_url(url)
        encoded_body = self.encode_body(body, kwargs)
        response = self.session.put(url, data=encoded_body, **kwargs)

        self.check_response(response, check_response)
        return response

    def encode_body(self, body, kwargs):
        raw = kwargs.pop('raw', None)
        if raw:
            return raw
        if body is not None:
            return json.dumps(body)
        return None

    def delete(self, url, **kwargs):
        kwargs.setdefault('headers', self.READ_HEADERS)
        check_response = kwargs.pop('check_response', True)

        url = self.clean_url(url)
        response = self.session.delete(url, **kwargs)

        self.check_response(response, check_response)
        return response
