# Copyright 2014-2022 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import CRUDCommand
from wazo_confd_client.relations import UserFuncKeyRelation
from wazo_confd_client.util import url_join


class TemplateRelation:
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
