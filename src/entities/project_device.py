from entities.project_point import ProjectPoint

class ProjectDevice:
    """This class is used to represent devices of a project. Device data is pulled from database
    and complemented by additional data that is project specific.
    
    Attributes:
        device_type: device type from database.
        device_points: points related to this device.
        device_position: device position, for composing point name.
        device_manufacturer: device manufacturer.
        point_name_separator: the character that separates different parts of point name.
    """
    def __init__(
            self,
            device_type:str,
            device_points:list,
            device_position:str,
            device_manufacturer:str,
            point_name_separator:str = "_"):
        """Constructor that creates project_device -objects.

        Args:
            device_type: type of this device.
            device_points: point data relating to this device.
            device_position: position of this device.
            device_manufacturer: manufacturer of this device.
            point_name_separator: used to separate different parts of point names.
        """

        self.__type = device_type

        self.__points = []
        # Create point objects from database point data.
        for entry in device_points:
            self.__points.append(
                ProjectPoint(device_position, entry, "NotImplemented", point_name_separator))

        self.__position = device_position
        self.__separator = point_name_separator
        self.__manufacturer = device_manufacturer


    def __check_valid(self, data:str):
        """Make sure given data only contains allowed characters.

        Args:
            data: data to be checked.

        Returns:
            True if check was passed, False if check failed.
        """

        allowed = "qwertyuiopåasdfghjklöäzxcvbnmQWERTYUIOPÅASDFGHJKLÖÄZXCVBNM,._1234567890+-"
        for character in data:
            if character not in allowed or character == self.__separator:
                return False
        return True

    def __update_point_names(self):
        """For updating this devices related point names.
        """
        for point in self.__points:
            point.device_position = self.__position

    def get_points(self):
        """Method that returns device points as list.

        Returns:
            data: list of point data related to this device. Formatted as tuples. 
        """
        data = []

        for point in self.points:
            data.append(point.get_point_data())

        return data

    @property
    def type(self):
        """For getting device attribute data.

        Returns:
            Attribute data:
        """
        return self.__type

    @property
    def points(self):
        """For getting device attribute data.

        Returns:
            Attribute data:
        """
        return self.__points

    @property
    def position(self):
        """For getting device position data.

        Returns:
            Attribute data:
        """
        return self.__position

    @property
    def manufacturer(self):
        """For getting device manufacturer data.

        Returns:
            Attribute data:
        """
        return self.__manufacturer

    @position.setter
    def position(self, position:str):
        """For setting the device position attribute.
        
        Args:
            position: new device position.
        """
        if self.__check_valid(position):
            self.__position = position
            self.__update_point_names()

    def to_csv(self):
        """For saving as csv.
        """
