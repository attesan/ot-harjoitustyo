class ProjectPoint:
    """Device that is added to project references a number of ProjectPoint objects that represent
    points configured for the device. Every point has a point name, for example AC1_TE1_AI.
    This class holds all information related to a point and methods for getting and setting.
    
    Attributes:
        self.__device_position: position of the parent device
        self.__point_position: position of this point
        self.__point_type: IO type of this point
        self.__separator: character that separeates point name sections.
        self.__point_name
        """
    def __init__(
            self,
            parent_device_position:str,
            point_position:str,
            point_type:str,
            point_name_separator:str = "_"):

        self.__device_position = parent_device_position
        self.__point_position = point_position
        self.__point_type = point_type
        self.__separator = point_name_separator
        self.__point_name = self.__compose_point_name()

    def __compose_point_name(self):
        """Compose point name from point data. 
        Use separator to separate different parts of the name.

        Returns:
            new_name: a full point name with parent device details.
        """
        new_name = self.__device_position + self.__separator
        new_name += self.point_position + self.__separator
        new_name += self.point_type
        return new_name

    def __check_valid(self, data:str):
        """Make sure given data only contains allowed characters.

        Args:
            data: data to be checked.

        Returns:
            True if check was passed, False if check failed.
        """
        allowed = "qwertyuiopåasdfghjklöäzxcvbnmQWERTYUIOPÅASDFGHJKLÖÄZXCVBNM,._1234567890+-"
        for characer in data:
            if characer not in allowed or characer == self.__separator:
                return False
        return True

    def get_point_data(self):
        """For getting point data as tuple.
        
        Returns: 
            Tuple containing relevant point data.
        """
        return (self.device_position, self.point_position, self.point_type, self.point_name)

    @property
    def point_type(self):
        """For getting attribute data.

        Returns:
            Attribute data:
        """
        return self.__point_type

    @property
    def point_position(self):
        """For getting attribute data.

        Returns:
            Attribute data:
        """
        return self.__point_position

    @property
    def device_position(self):
        """For getting attribute data.

        Returns:
            Attribute data:
        """
        return self.__device_position

    @property
    def point_name(self):
        """For getting attribute data.

        Returns:
            Attribute data:
        """
        return self.__point_name

    @point_type.setter
    def point_type(self, point_type:str):
        """For setting attribute data. Validates given data before setting it.

        Args:
            point_type: attribute to be changed.
        """
        if self.__check_valid(point_type):
            self.__point_type = point_type
            self.__point_name = self.__compose_point_name()

    @point_position.setter
    def point_position(self, point_position:str):
        """For setting attribute data. Validates given data before setting it.

        Args:
            point_position: attribute to be changed.
        """
        if self.__check_valid(point_position):
            self.__point_position = point_position
            self.__point_name = self.__compose_point_name()

    @device_position.setter
    def device_position(self, device_position:str):
        """For setting attribute data. Validates given data before setting it.

        Args:
            device_position: attribute to be changed.
        """
        if self.__check_valid(device_position):
            self.__device_position = device_position
            self.__point_name = self.__compose_point_name()

    def to_csv(self):
        """For getting point data in csv form.
        """

        data = str(self.__point_name)
        return data
