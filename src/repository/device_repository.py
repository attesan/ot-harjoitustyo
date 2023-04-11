import os
from pathlib import Path
from database_connection import get_database_connection

class DeviceRepository:
    #This class is responsible for saving new devices into database and fetching saved devices.
    def __init__(self, ):
        self._connection = get_database_connection()

    def new_device(self):
        pass

    def search_device(self):
        pass

    def delete_device(self):
        pass

    def delete_repository(self):
        os.remove(self._connection)
