# Copyright 2017-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import CRUDCommand


class ExtensionsFeaturesCommand(CRUDCommand):

    resource = 'extensions/features'

    def create(self):
        raise NotImplementedError()

    def delete(self):
        raise NotImplementedError()
