import unittest
import os
import initialize_database

class TestInitializeDatabase(unittest.TestCase):
    def setUp(self):
        self.devices = initialize_database.initialize_database()

    def test_create(self):
        pass