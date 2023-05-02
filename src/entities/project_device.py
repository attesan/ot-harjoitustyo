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
        """Constructor that creates project_device.
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
        """Check that given data only has allowed characters.

        Attributes: 
            data: data to check.
        """
        allowed = "qwertyuiopåasdfghjklöäzxcvbnmQWERTYUIOPÅASDFGHJKLÖÄZXCVBNM,._1234567890+-"
        for character in data:
            if character not in allowed or character == self.__separator:
                return False
        return True

    def __update_point_names(self):
        """Update this devices points names"""
        for point in self.__points:
            point.device_position = self.__position

    def get_points(self):
        """Class that returns device points as list"""
        data = []

        # Get point data for every point.
        for point in self.points:
            data.append(point.get_point_data())

        return data

    @property
    def type(self):
        return self.__type

    @property
    def points(self):
        return self.__points

    @property
    def position(self):
        return self.__position

    @property
    def manufacturer(self):
        return self.__manufacturer

    # Setter methods for changing data
    @position.setter
    def position(self, position:str):
        """For setting the device position attribute
        
        Args:
            position: new device position"""
        # Check data is valid before updating related point data
        if self.__check_valid(position):
            self.__position = position
            self.__update_point_names()

    def to_csv(self):
        """For saving as csv"""
        pass
