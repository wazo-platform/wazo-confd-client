# -*- coding: UTF-8 -*-
# Copyright (C) 2015 Avencall
# SPDX-License-Identifier: GPL-3.0+

from xivo_lib_rest_client import HTTPCommand
from xivo_confd_client.util import url_join
from xivo_confd_client.relations import UserCtiProfileRelation
from xivo_confd_client.util import extract_id


class CtiProfileRelation(object):

    def __init__(self, builder, cti_profile_id):
        self.cti_profile_id = cti_profile_id
        self.user_cti_profile = UserCtiProfileRelation(builder)

    @extract_id
    def add_user(self, user_id):
        self.user_cti_profile.associate(user_id, self.cti_profile_id)


class CtiProfilesCommand(HTTPCommand):

    def list(self):
        url = url_join('cti_profiles')
        r = self.session.get(url)

        return r.json()

    def get(self, cti_profile_id):
        url = url_join('cti_profiles', cti_profile_id)
        r = self.session.get(url)

        return r.json()
