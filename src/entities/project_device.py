from entities.project_point import ProjectPoint

class ProjectDevice:
    # This class is used to represent devices of a project. Device data is pulled from database
    # and complemented by additional data that is project specific.
    def __init__(
            self,
            device_type:str,
            device_points:list,
            device_position:str,
            point_name_separator:str = "_"):

        self.__type = device_type

        self.__points = []
        # Create point objects from database point data.
        for entry in device_points:
            self.__points.append(
                ProjectPoint(device_position, entry, "NotImplemented", point_name_separator))

        self.__position = device_position
        self.__separator = point_name_separator

    # Make sure given data is in correct form
    def __check_valid(self, data):
        allowed = "qwertyuiopåasdfghjklöäzxcvbnmQWERTYUIOPÅASDFGHJKLÖÄZXCVBNM,._1234567890+-"
        for character in data:
            if character not in allowed or character == self.__separator:
                return False
        return True

    # Update related point objects with new device position
    def __update_point_names(self):
        for point in self.__points:
            point.device_position = self.__position

    # Getter methods
    @property
    def type(self):
        return self.__type

    @property
    def points(self):
        return self.__points

    @property
    def position(self):
        return self.__position

    # Setter methods for changing data
    @position.setter
    def position(self, position):
        # Check data is valid before updating related point data
        if self.__check_valid(position):
            self.__position = position
            self.__update_point_names()

    # For getting device data in csv friendly form. It is here for now. Might change into
    # something else like point data in list form.
    def to_csv(self):
        pass
