import unittest
import os
from initialize_database import InitializeDatabase

class TestInitializeDatabase(unittest.TestCase):
    def setUp(self):
        devices = InitializeDatabase.initialize_database()

    def test_create(self):
        pass