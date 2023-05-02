import os
import sys
import entities.project_device as project_device

sys.path.insert(0, os.path.abspath(".."))

class ProjectDataService:
    # This class keeps track of all devices that are added to a project.
    # Using dict to help make sure only one device exists for a given device position.
    def __init__(self):
        self.__devices = {}

    # Add one device for a given position.
    def add_device(self, device:project_device):
        self.__devices[device.position] = device

    # Return list of devices added to project.
    def get_device_list(self):
        return self.__devices

    # Return dictionary of points from every device added to project.
    def get_point_list(self):
        points = {}

        for key in self.__devices:
            points[key] = self.__devices[key].get_points()

        return points

    # Remove a device from project.
    def remove_device(self, position:str):
        self.__devices.pop(position)

    # Get device data in csv format.
    def to_csv(self):
        pass