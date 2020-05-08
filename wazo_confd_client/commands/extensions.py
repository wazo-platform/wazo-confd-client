# -*- coding: utf-8 -*-
# Copyright 2016-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.util import extract_id
from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import LineExtensionRelation


class ExtensionRelation(object):
    def __init__(self, builder, extension_id):
        self.extension_id = extension_id
        self.line_extension_relation = LineExtensionRelation(builder)

    @extract_id
    def add_line(self, line_id):
        return self.line_extension_relation.associate(line_id, self.extension_id)

    @extract_id
    def remove_line(self, line_id):
        return self.line_extension_relation.dissociate(line_id, self.extension_id)


class ExtensionsCommand(MultiTenantCommand):

    resource = 'extensions'

    relation_cmd = ExtensionRelation
