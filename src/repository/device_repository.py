import os
from pathlib import Path
from database_connection import get_database_connection


class DeviceRepository:
    # This class is responsible for saving new devices into database and fetching saved devices.
    def __init__(self, ):
        self._connection = get_database_connection()

    # Add new device into database
    def new_device(self, device_model, device_manufacturer, device_points):
        cursor = self._connection.cursor()

        # Add device to Devices -table
        cursor.execute(
            "insert into Devices (model, manufacturer) values (?, ?)", 
            (device_model, device_manufacturer)
        )

        # Get row id of device that was just created
        device_id = cursor.lastrowid

        # Add points to DevicePoints -table
        # For now device_points is a list of point-data tuples (device_id, point_name, point_type)
        for p in device_points:
            if p[0] != None:
                cursor.execute(
                    "insert into DevicePoints (device_id, point_name, point_text, point_type) values (?, ?, ?, ?)",
                    (device_id, p[0], p[1], p[2])
                )

    # Search for device by model name
    def search_by_model(self, search_word):
        cursor = self._connection.cursor()

        return cursor.execute(
            "select * from Devices where model = ?", 
            (search_word,)
        ).fetchone()

    # Get all devices
    def find_all_devices(self):
        cursor = self._connection.cursor()

        return cursor.execute(
            "select * from devices"
        ).fetchall()

    # Not implemented yet
    def delete_device(self):
        pass

    # Delete the database file, implemented in case it is needed
    def delete_repository(self):
        os.remove(self._connection)

    # Delete everything from all tables
    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute("delete from Devices")
        cursor.execute("delete from DevicePoints")
        cursor.execute("delete from DeviceData")