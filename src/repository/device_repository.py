from database_connection import get_database_connection

class DeviceRepository:
    """This class is responsible for saving new devices into database and fetching saved devices.
    
    Attributes: 
        _connection: database connection.
    """
    def __init__(self, ):
        self._connection = get_database_connection()

    def new_device(self, device_model, device_manufacturer, device_points):
        """For adding new devices into database.
        
        Args:
            device_model: model of the device.
            device_manufacturer: manufacturer of the device.
            device_points: list of points relating to this device.
        """
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

    def search_device_data_by_id(self,search_id:int):
        """For searching device and its related points by device id.
        
        Args:
            search_id: id of device to be searched.

        Returns: 
            Tuple containing device data and points that resulted from database search.
        """
        cursor = self._connection.cursor()

        # Get device data.
        device_data = cursor.execute(
            "SELECT * FROM Devices WHERE Id = ?;",
            (search_id,)
        ).fetchone()

        # Get device points data.
        device_points = cursor.execute(
            """SELECT DP.point_name, DP.point_text, DP.point_type 
            FROM DevicePoints DP, Devices D 
            WHERE D.id = ? AND D.id = DP.device_id""",
            (search_id,)
        ).fetchall()

        return (device_data, device_points)

    # Search for device by model name
    def search_by_model(self, search_word:str):
        """For searching device by model.
        
        Args:
            search_word: device model to be searched

        Returns:
            One row from the database search.
        """
        cursor = self._connection.cursor()

        return cursor.execute(
            "SELECT * FROM Devices WHERE model = ?;", 
            (search_word,)
        ).fetchone()

    def find_all_devices(self):
        """For retrieving all devices.

        Returns:
            All devices from the database.
        """
        cursor = self._connection.cursor()

        return cursor.execute(
            "SELECT * FROM devices;"
        ).fetchall()

    def find_device_points(self, search_word:str):
        """Get all points related to a device.

        Args:
            search_word: device model to be searched.

        Returns:
            All resulting rows of database search.
        """
        cursor = self._connection.cursor()

        return cursor.execute(
            """SELECT DP.point_name, DP.point_text, DP.point_type 
            FROM DevicePoints DP, Devices D 
            WHERE D.id = DP.device_id and D.model = ?;"""
            , (search_word,)
        ).fetchall()

    def update_device(self, device_id, device_model, device_manufacturer, device_points):
        """Update a database entry.
        
        Args:
            device_id: new id for device
            device_model: new model for device
            device_manufacturer: new manufacturer for device
            device_points: new points for device
        """
        cursor = self._connection.cursor()

        cursor.execute(
            """UPDATE Devices 
            SET model = ?, manufacturer = ?
            WHERE id = ?;""",
            (device_model, device_manufacturer, device_id)
        )

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

    def delete_all(self):
        """Delete everything from all tables
        """
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM Devices;")
        cursor.execute("DELETE FROM DevicePoints;")
        cursor.execute("DELETE FROM DeviceData;")
        