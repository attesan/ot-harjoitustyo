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
        """Constructor for the class. 
        Initializes an empty dict for keeping track of project devices.
        """
        self.__devices = {}

    def add_device(self, device:ProjectDevice):
        """Check if device position is not yet used.
        Add one device for a given position if it is free. 
        
        Args:
            device: ProjectDevice -object to be added.

        Return:
            None if device with given position already exists.
            True if device added successfully.
        """
        try:
            self.__devices[device.position] = device
            return True
        except: # pylint: disable=bare-except
            return False

    def get_device_list(self):
        """Return list of devices added to project.

        Return: 
            __devices: list of added devices.
        """
        return self.__devices

    def get_point_list(self):
        """Return dictionary of points from every device added to project.

        Return:
            points: dictionary key=device_position, values=list of points for all devices.
        """
        points = {}

        for device_position, device in self.__devices.items():
            points[device_position] = device.get_points()

        return points

    def remove_device(self, position:str):
        """Remove a device from project.
        
        Args:
            position: device position of the device to be removed
        """
        self.__devices.pop(position)

    def get_csv(self):
        """For getting project data in csv friendly format.
        """
        data = []
        for device in self.__devices.values():
            device_data = device.to_csv()
            data.append(device_data)

        return data
