class ProjectPoint:
    # Device that is added to project references a number of ProjectPoint objects that represent
    # points configured for the device. Every point has a point name, for example AC1_TE1_AI.
    # This class holds all information related to a point and methods for getting and setting.
    def __init__(
            self,
            parent_device_position:str,
            point_position:str,
            point_type:str,
            point_name_separator:str = "_"):
        self.__point_type = point_type
        self.__point_position = point_position
        self.__device_position = parent_device_position
        self.__separator = point_name_separator
        self.__point_name = self.__compose_point_name()

    # Compose point name
    def __compose_point_name(self):
        new_name = self.__device_position + self.__separator
        new_name += self.point_position + self.__separator
        new_name += self.point_type
        return new_name

    # Make sure given data is in correct form
    def __check_valid(self, data):
        allowed = "qwertyuiopåasdfghjklöäzxcvbnmQWERTYUIOPÅASDFGHJKLÖÄZXCVBNM,._1234567890+-"
        for characer in data:
            if characer not in allowed or characer == self.__separator:
                return False
        return True

    # Getters
    @property
    def point_type(self):
        return self.__point_type

    @property
    def point_position(self):
        return self.__point_position

    @property
    def device_position(self):
        return self.__device_position

    @property
    def point_name(self):
        return self.__point_name

    # setters
    @point_type.setter
    def point_type(self, point_type):
        if self.__check_valid(point_type):
            self.__point_type = point_type
            self.__point_name = self.__compose_point_name()

    @point_position.setter
    def point_position(self, point_position):
        if self.__check_valid(point_position):
            self.__point_position = point_position
            self.__point_name = self.__compose_point_name()

    @device_position.setter
    def device_position(self, device_position):
        if self.__check_valid(device_position):
            self.__device_position = device_position
            self.__point_name = self.__compose_point_name()
