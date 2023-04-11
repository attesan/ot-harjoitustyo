import unittest
import os
import sys
from repository.device_repository import DeviceRepository

sys.path.insert(0, os.path.abspath(".."))


class TestDeviceDatabase(unittest.TestCase):
    def setUp(self):
        self.d = DeviceRepository()

    def test_database_exists(self):
        print("testi",os.path)
        self.assertEqual(os.path.exists("../data/devices.db"), True)