# -*- coding: UTF-8 -*-

# Copyright (C) 2015 Avencall
# Copyright (C) 2016 Proformatique Inc.
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
    def wrapper(self, resource_or_id, **kwargs):
        if isinstance(resource_or_id, dict):
            resource_id = resource_or_id['id']
        else:
            resource_id = resource_or_id
        return func(self, resource_id, **kwargs)
    return wrapper
