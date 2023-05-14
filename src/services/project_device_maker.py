import os
import sys
from entities.project_device import ProjectDevice
from repository.device_repository import DeviceRepository

sys.path.insert(0, os.path.abspath(".."))

class ProjectDeviceMaker:
    """This class turns database data into project_device -objects.
    
    Attributes:
        _devices: database connection.
    """
    def __init__(self):
        """Constructor for class. Sets attributes initial values.
        """
        self._devices = DeviceRepository()

    def make_project_device(self, device_position:str ,device_id:int):
        """Make device for project_data_service.
        
        Args:
            device_position: position of device.
            device_id: device id for database search.

        Returns:
            new_project_device: a ProjectDevice -object.
        """
        # Get (device_data, point_data) tuple from repository.
        data = self.__get_device_data(device_id)
        point_positions = []

        for row in data[1]:
            if row[0] != "":
                point_positions.append(row[0])

        new_project_device = ProjectDevice(data[0][1],point_positions,device_position,data[0][2])
        return new_project_device

    def __get_device_data(self, device_id:int):
        """For getting device and point data from repository.
        
        Args:
            device_id: device id to be searched.
        """
        data = self._devices.search_device_data_by_id(device_id)
        return data
