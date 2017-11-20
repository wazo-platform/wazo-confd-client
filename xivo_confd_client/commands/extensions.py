# -*- coding: utf-8 -*-
# Copyright (C) 2015-2016 Avencall
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import LineExtensionRelation


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

    def get_line(self):
        return self.line_extension_relation.get_by_extension(self.extension_id)

    def list_lines(self):
        return self.line_extension_relation.list_by_extension(self.extension_id)


class ExtensionsCommand(CRUDCommand):

    resource = 'extensions'

    relation_cmd = ExtensionRelation
