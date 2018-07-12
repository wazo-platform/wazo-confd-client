# -*- coding: utf-8 -*-
# Copyright 2018 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from xivo_confd_client.crud import CRUDCommand


class SkillsCommand(CRUDCommand):

    resource = 'agents/skills'
