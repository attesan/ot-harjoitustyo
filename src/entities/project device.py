class ProjectDevice:
    # This class is used when adding devices to a project. Device data is pulled from database
    # and complemented by additional data that is project specific. Project specific data is not added
    # to database because it can be different in every project.
    def __init__(self, device_type, device_points):
        self._type = device_type
        self._points = device_points
        self._position = ""