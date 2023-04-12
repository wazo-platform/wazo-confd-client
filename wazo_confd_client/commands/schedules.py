# Copyright 2017-2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_confd_client.crud import MultiTenantCommand


class SchedulesCommand(MultiTenantCommand):
    resource = 'schedules'
