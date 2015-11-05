# -*- coding: utf-8 -*-

# Copyright (C) 2015 Avencall
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
from xivo_confd_client.util import extract_id
from xivo_confd_client.relations import UserLineRelation, LineExtensionRelation


class LineSIPRelation(object):

    def __init__(self, builder, line_id):
        self.line_id = line_id
        self.line_extension_relation = LineExtensionRelation(builder)
        self.user_line_relation = UserLineRelation(builder)

    @extract_id
    def add_extension(self, extension_id):
        return self.line_extension_relation.associate(self.line_id, extension_id)

    @extract_id
    def remove_extension(self, extension_id):
        return self.line_extension_relation.dissociate(self.line_id, extension_id)

    def list_extensions(self):
        return self.line_extension_relation.list_by_line(self.line_id)

    @extract_id
    def add_user(self, user_id):
        return self.user_line_relation.associate(user_id, self.line_id)

    @extract_id
    def remove_user(self, user_id):
        return self.user_line_relation.dissociate(user_id, self.line_id)

    @extract_id
    def list_users(self):
        return self.user_line_relation.list_by_line(self.line_id)


class LinesSIPCommand(CRUDCommand):

    resource = 'lines_sip'

    relation_cmd = LineSIPRelation
