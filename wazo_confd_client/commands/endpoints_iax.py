# Copyright 2018-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand


class EndpointsIAXCommand(MultiTenantCommand):
    resource = 'endpoints/iax'
