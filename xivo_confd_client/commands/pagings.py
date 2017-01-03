# -*- coding: utf-8 -*-

# Copyright 2017 The Wazo Authors  (see the AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import PagingCallerUserRelation, PagingMemberUserRelation


class PagingRelation(object):

    def __init__(self, builder, paging_id):
        self.paging_id = paging_id
        self.paging_user_callers = PagingCallerUserRelation(builder)
        self.paging_user_members = PagingMemberUserRelation(builder)

    def update_user_members(self, users):
        return self.paging_user_members.associate(self.paging_id, users)

    def update_user_callers(self, users):
        return self.paging_user_members.associate(self.paging_id, users)


class PagingsCommand(CRUDCommand):

    resource = 'pagings'
    relation_cmd = PagingRelation
