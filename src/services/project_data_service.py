import os
import sys
from entities.project_device import ProjectDevice

sys.path.insert(0, os.path.abspath(".."))

class ProjectDataService:
    # This class is a project data manager.
    # It keeps track of all devices that are added to a project. Also offers methods for
    # getting useful project data.
    # Using dict to help make sure only one device exists for a given device position.
    def __init__(self):
        self.__devices = {}

    # Add one device for a given position.
    def add_device(self, device:ProjectDevice):
        self.__devices[device.position] = device

    # Return list of devices added to project.
    def get_device_list(self):
        return self.__devices

    # Return dictionary of points from every device added to project.
    def get_point_list(self):
        points = {}

        for device_position, device in self.__devices.items():
            points[device_position] = device.get_points()

        return points

    # Remove a device from project.
    def remove_device(self, position:str):
        self.__devices.pop(position)

    # Get device data in csv format.
    def to_csv(self):
        pass
