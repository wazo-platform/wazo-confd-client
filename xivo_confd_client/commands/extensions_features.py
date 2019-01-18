# -*- coding: utf-8 -*-
# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from xivo_confd_client.crud import CRUDCommand


class ExtensionsFeaturesCommand(CRUDCommand):

    resource = 'extensions/features'

    def create(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()
