# -*- coding: utf-8 -*-
# Copyright 2016-2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import (
    TrunkEndpointSipRelation,
    TrunkEndpointIAXRelation,
    TrunkEndpointCustomRelation,
    TrunkRegisterSipRelation,
    TrunkRegisterIAXRelation,
)


class TrunkRelation(object):

    def __init__(self, builder, trunk_id):
        self.trunk_id = trunk_id
        self.trunk_endpoint_sip = TrunkEndpointSipRelation(builder)
        self.trunk_endpoint_iax = TrunkEndpointIAXRelation(builder)
        self.trunk_endpoint_custom = TrunkEndpointCustomRelation(builder)
        self.trunk_register_iax = TrunkRegisterIAXRelation(builder)
        self.trunk_register_sip = TrunkRegisterSipRelation(builder)

    @extract_id
    def add_endpoint_sip(self, endpoint_sip_id):
        return self.trunk_endpoint_sip.associate(self.trunk_id, endpoint_sip_id)

    @extract_id
    def remove_endpoint_sip(self, endpoint_sip_id):
        return self.trunk_endpoint_sip.dissociate(self.trunk_id, endpoint_sip_id)

    def get_endpoint_sip(self):
        return self.trunk_endpoint_sip.get_by_trunk(self.trunk_id)

    @extract_id
    def add_endpoint_iax(self, endpoint_iax_id):
        return self.trunk_endpoint_iax.associate(self.trunk_id, endpoint_iax_id)

    @extract_id
    def remove_endpoint_iax(self, endpoint_iax_id):
        return self.trunk_endpoint_iax.dissociate(self.trunk_id, endpoint_iax_id)

    @extract_id
    def add_endpoint_custom(self, endpoint_custom_id):
        return self.trunk_endpoint_custom.associate(self.trunk_id, endpoint_custom_id)

    @extract_id
    def remove_endpoint_custom(self, endpoint_custom_id):
        return self.trunk_endpoint_custom.dissociate(self.trunk_id, endpoint_custom_id)

    def get_endpoint_custom(self):
        return self.trunk_endpoint_custom.get_by_trunk(self.trunk_id)

    @extract_id
    def add_register_sip(self, register_sip_id):
        return self.trunk_register_sip.associate(self.trunk_id, register_sip_id)

    @extract_id
    def remove_register_sip(self, register_sip_id):
        return self.trunk_register_sip.dissociate(self.trunk_id, register_sip_id)

    @extract_id
    def add_register_iax(self, register_iax_id):
        return self.trunk_register_iax.associate(self.trunk_id, register_iax_id)

    @extract_id
    def remove_register_iax(self, register_iax_id):
        return self.trunk_register_iax.dissociate(self.trunk_id, register_iax_id)


class TrunksCommand(CRUDCommand):

    resource = 'trunks'
    relation_cmd = TrunkRelation
