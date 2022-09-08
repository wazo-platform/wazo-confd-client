# -*- coding: utf-8 -*-
# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_lib_rest_client.command import RESTCommand

from .exceptions import ConfdClientError


class ConfdCommand(RESTCommand):
    @staticmethod
    def raise_from_response(response):
        raise ConfdClientError(response)
