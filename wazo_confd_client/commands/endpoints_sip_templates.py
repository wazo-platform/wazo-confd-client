# Copyright 2020-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand


class EndpointsSipTemplatesCommand(MultiTenantCommand):
    resource = 'endpoints/sip/templates'
