# -*- coding: utf-8 -*-
# Copyright (C) 2014-2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import HTTPCommand


class InfosCommand(HTTPCommand):

    def __call__(self):
        return self.get()

    def get(self):
        r = self.session.get('/infos')

        return r.json()
