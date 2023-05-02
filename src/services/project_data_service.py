import os
import sys
from entities.project_device import ProjectDevice

sys.path.insert(0, os.path.abspath(".."))

class ProjectDataService:
    """This class is a project data manager.
    It keeps track of all devices that are added to a project. Also offers methods for
    getting useful project data.
    Using dict to help make sure only one device exists for a given device position.
    
    Attributes:
        __devices: dictionary for project devices
    """
    def __init__(self):
        """Constructor for the class."""
        self.__devices = {}

    def add_device(self, device:ProjectDevice):
        """Add one device for a given position.
        
        Args:
            device: ProjectDevice -object to be added
        """
        self.__devices[device.position] = device

    def get_device_list(self):
        """Return list of devices added to project.
        """
        return self.__devices

    def get_point_list(self):
        """Return dictionary of points from every device added to project.
        """
        points = {}

        for device_position, device in self.__devices.items():
            points[device_position] = device.get_points()

        return points

    def remove_device(self, position:str):
        """Remove a device from project.
        
        Args:
            position: device position of the device to be removed"""
        self.__devices.pop(position)

    def to_csv(self):
        """Get device data in csv format."""
        pass
