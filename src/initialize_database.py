import os
import sys
from database_connection import get_database_connection  # From materials

sys.path.insert(0, os.path.abspath(".."))

# Create device, point and data tables in the database
def create_tables(connection):
    cursor = connection.cursor()

    # Device model and manufacturer in this table
    cursor.execute(
        """create table Devices 
        (id integer primary key, 
        model text, 
        manufacturer text);""")

    # Points related to device go here, identified by Device_id, type is for possible future use
    # for example: DI,DO,AI,AO,FDI,FDO,FAI,FAO
    cursor.execute(
        """create table DevicePoints 
        (id integer primary key, 
        device_id integer, 
        pointname text, type text);""")

    # For possible future use, here you can save device data such as voltage, amps, power,
    # reaction time, dimensions, k-value, etc. You can also save a text key to explain
    # the who-knows-what that is that is in data_value column
    cursor.execute(
        """create table DeviceData (id integer primary key, 
        device_id integer, 
        data_value real, 
        data_information text);""")

    connection.commit()

# Drop all tables
def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("drop table if exists Devices;")
    cursor.execute("drop table if exists DevicePoints;")
    cursor.execute("drop table if exists DeviceData;")
    connection.commit()

# Drop all tables and make new ones
def initialize_database():  
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
