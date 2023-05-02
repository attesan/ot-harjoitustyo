import os
import sqlite3

directory_name = os.path.dirname(__file__)
connection = sqlite3.connect(os.path.join(
    directory_name, "data", "devices.db"))
connection.row_factory = sqlite3.Row


def get_database_connection():
    """For returning database connection.
    
    Returns: 
        database connections
    """
    return connection
