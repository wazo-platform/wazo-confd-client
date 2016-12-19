# -*- coding: utf-8 -*-

# Copyright 2016 The Wazo Authors  (see the AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from xivo_confd_client.util import extract_id
from xivo_confd_client.crud import CRUDCommand
from xivo_confd_client.relations import ParkingLotExtensionRelation


class ParkingLotRelation(object):

    def __init__(self, builder, parking_lot_id):
        self.parking_lot_id = parking_lot_id
        self.parking_lot_extension = ParkingLotExtensionRelation(builder)

    @extract_id
    def add_extension(self, extension_id):
        return self.parking_lot_extension.associate(self.parking_lot_id, extension_id)

    @extract_id
    def remove_extension(self, extension_id):
        return self.parking_lot_extension.dissociate(self.parking_lot_id, extension_id)


class ParkingLotsCommand(CRUDCommand):

    resource = 'parkinglots'
    relation_cmd = ParkingLotRelation
