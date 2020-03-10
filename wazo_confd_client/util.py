# -*- coding: utf-8 -*-
# Copyright 2015-2017 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import unicode_literals

from functools import wraps
from six import text_type


def url_join(*parts):
    return "/" + "/".join(text_type(p) for p in parts)


def extract_id(func):
    @wraps(func)
    def wrapper(self, resource_or_id, *args, **kwargs):
        if isinstance(resource_or_id, dict):
            if 'id' in resource_or_id:
                resource_id = resource_or_id['id']
            elif 'uuid' in resource_or_id:
                resource_id = resource_or_id['uuid']
            else:
                raise KeyError('no id or uuid key found')
        else:
            resource_id = resource_or_id
        return func(self, resource_id, *args, **kwargs)

    return wrapper
