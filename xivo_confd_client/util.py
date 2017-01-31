# -*- coding: UTF-8 -*-

# Copyright 2015-2017 The Wazo Authors  (see the AUTHORS file)
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

from __future__ import unicode_literals

from functools import wraps


def url_join(*parts):
    return "/" + "/".join(unicode(p) for p in parts)


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
