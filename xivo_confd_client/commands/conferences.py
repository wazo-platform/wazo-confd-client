# -*- coding: utf-8 -*-
# Copyright 2016 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import ConferenceExtensionRelation


class ConferenceRelation(object):

    def __init__(self, builder, conference_id):
        self.conference_id = conference_id
        self.conference_extension = ConferenceExtensionRelation(builder)

    @extract_id
    def add_extension(self, extension_id):
        return self.conference_extension.associate(self.conference_id, extension_id)

    @extract_id
    def remove_extension(self, extension_id):
        return self.conference_extension.dissociate(self.conference_id, extension_id)


class ConferencesCommand(CRUDCommand):

    resource = 'conferences'
    relation_cmd = ConferenceRelation
