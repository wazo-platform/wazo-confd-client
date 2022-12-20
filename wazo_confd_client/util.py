# Copyright 2015-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later
from functools import wraps


def url_join(*parts):
    return "/" + "/".join(str(p) for p in parts)


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


def extract_name(pass_original=False):
    def decorator(func):
        @wraps(func)
        def wrapper(self, resource_or_id, *args, **kwargs):
            if isinstance(resource_or_id, dict):
                if 'name' in resource_or_id:
                    resource_id = resource_or_id['name']
                else:
                    raise KeyError('no "name" key found')
            else:
                resource_id = resource_or_id
            if pass_original:
                return func(self, resource_id, resource_or_id, *args, **kwargs)
            else:
                return func(self, resource_id, *args, **kwargs)

        return wrapper

    return decorator
