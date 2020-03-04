# -*- coding: utf-8 -*-
# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.util import url_join
from wazo_confd_client.crud import CRUDCommand


class AccessFeaturesCommand(CRUDCommand):

    resource = 'access_features'
