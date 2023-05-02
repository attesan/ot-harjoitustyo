import os
import sys
from entities.project_device import ProjectDevice
from repository.device_repository import DeviceRepository

sys.path.insert(0, os.path.abspath(".."))

class ProjectDeviceMaker:
    # This class turns database data into project_device -objects.
    def __init__(self):
        self._devices = DeviceRepository()

    # Make device for project_data_service.
    def make_project_device(self, device_position:str ,device_id:int):
        # Get (device_data, point_data) tuple from repository.
        data = self.__get_device_data(device_id)
        point_positions = []

        # Convert from sqlite3 row-objects to list for project_point object creation.
        for row in data[1]:
            point_positions.append(row[2])

        # Make new ProjectDevice -object.
        new_project_device = ProjectDevice(data[0][1],point_positions,device_position,data[0][2])
        return new_project_device

    # Get data from repository.
    def __get_device_data(self, device_id:int):
        data = self._devices.search_device_data_by_id(device_id)
        return data
