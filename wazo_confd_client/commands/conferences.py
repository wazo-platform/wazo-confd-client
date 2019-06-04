# -*- coding: utf-8 -*-
# Copyright 2016-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.util import extract_id
from wazo_confd_client.crud import MultiTenantCommand
from wazo_confd_client.relations import ConferenceExtensionRelation


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


class ConferencesCommand(MultiTenantCommand):

    resource = 'conferences'
    relation_cmd = ConferenceRelation
