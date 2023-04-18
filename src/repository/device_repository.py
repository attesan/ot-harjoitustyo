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
            """INSERT INTO Devices 
            (model, manufacturer) 
            VALUES (?, ?);""", 
            (device_model, device_manufacturer)
        )

        # Get row id of device that was just created
        device_id = cursor.lastrowid

        # Add points to DevicePoints -table
        # For now device_points is a list of point names
        for point in device_points:
            if point is not None:
                cursor.execute(
                    """INSERT INTO DevicePoints 
                    (device_id, point_name, point_text, point_type) 
                    VALUES (?, ?, ?, ?);""",
                    (device_id, point[0],"not implemented","not implemented")
                )

        self._connection.commit()

    # Search for device by model name
    def search_by_model(self, search_word):
        cursor = self._connection.cursor()

        return cursor.execute(
            "SELECT * FROM Devices WHERE model = ?;", 
            (search_word,)
        ).fetchone()

    # Get all devices
    def find_all_devices(self):
        cursor = self._connection.cursor()

        return cursor.execute(
            "SELECT * FROM devices;"
        ).fetchall()

    # Get all points related to a device
    def find_device_points(self, search_word):
        cursor = self._connection.cursor()

        return cursor.execute(
            """SELECT DP.point_name, DP.point_text, DP.point_type 
            FROM DevicePoints DP, Devices D 
            WHERE D.id = DP.device_id and D.model = ?;"""
            , (search_word,)
        ).fetchall()

    # Update a database entry not implemented yet
    def update_device(self, device_id, device_model, device_manufacturer, device_points):
        cursor = self._connection.cursor()

        # Update Devices table
        cursor.execute(
            """UPDATE Devices 
            SET model = ?, manufacturer = ?
            WHERE id = ?;""",
            (device_model, device_manufacturer, device_id)
        )

        # Update DevicePoints table
        i = 0
        for point in device_points:
            cursor.execute(
                """UPDATE DevicePoints
                SET point_name = ?
                WHERE device_id = ? AND id = ?;""",
                (point[0], device_id, i)
            )
            i += 1

        self._connection.commit()

    # Not implemented yet
    def delete_device(self):
        pass

    # Delete everything from all tables
    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Devices;")
        cursor.execute("DELETE FROM DevicePoints;")
        cursor.execute("DELETE FROM DeviceData;")
        