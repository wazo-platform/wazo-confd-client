# -*- coding: UTF-8 -*-

# Copyright (C) 2015 Avencall
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
