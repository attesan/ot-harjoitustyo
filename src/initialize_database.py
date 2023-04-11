from database_connection import get_database_connection #From materials

def create_tables(connection):
    cursor = connection.cursor()

    #Device model and manufacturer in this table
    cursor.execute(
        '''create table Devices 
        (id integer primary key, 
        model text, 
        manufacturer text) 
        if not exists Devices;''')

    #Points related to device go here, identified by Device_id, type is for possible future use
    #and will be limited to following: DI,DO,AI,AO,FDI,FDO,FAI,FAO
    cursor.execute(
        '''create table DevicePoints 
        (id integer primary key, 
        device_id integer, 
        pointname text, type text) 
        if not exists DevicePoints;''')

    #For possible future use, here you can save device data such as voltage, amps, power,
    #reaction time, dimensions, k-value, etc. You can also save a text key to help explain
    #the who-knows-what-that-is that is in data_value
    cursor.execute(
        '''create table DeviceData (id integer primary key, 
        device_id integer, 
        data_value real, 
        data_information text) 
        if not exists DevicePoints;''')

    connection.commit()

    #Clear data in tables
def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("drop table if exists Devices;")
    cursor.execute("drop table if exists DevicePoints;")
    cursor.execute("drop table if exists DeviceData;")
    connection.commit()

def initialize_database(): #Get database connection
    connection = get_database_connection()
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
