# -*- coding: utf-8 -*-

# Copyright (C) 2014-2015 Avencall
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
from xivo_confd_client.relations import UserFuncKeyRelation
from xivo_confd_client.util import url_join


class TemplateRelation(object):

    def __init__(self, builder, template_id):
        self.template_id = template_id
        self.user_funckey = UserFuncKeyRelation(builder)

    def add_user(self, user_id):
        self.user_funckey.associate_template(user_id, self.template_id)

    def remove_user(self, user_id):
        self.user_funckey.dissociate_template(user_id, self.template_id)


class FuncKeysCommand(CRUDCommand):

    resource = 'funckeys/templates'
    relation_cmd = TemplateRelation

    def get_template_funckey(self, template_id, position):
        url = url_join(self.resource, template_id, position)
        response = self.session.get(url)
        return response.json()

    def delete_template_funckey(self, template_id, position):
        url = url_join(self.resource, template_id, position)
        self.session.delete(url)

    def update_template_funckey(self, template_id, position, funckey):
        url = url_join(self.resource, template_id, position)
        self.session.put(url, funckey)
