# -*- coding: utf-8 -*-
# Copyright 2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later


class ConfdClientError(Exception):
    def __init__(self, error):
        super(ConfdClientError, self).__init__(error)
        self.error = error
