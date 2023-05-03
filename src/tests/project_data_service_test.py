import unittest
import os
import sys
from services.project_data_service import ProjectDataService
from entities.project_device import ProjectDevice

sys.path.insert(0, os.path.abspath(".."))

class TestProjectDataService(unittest.TestCase):
    def setUp(self):
        self.service = ProjectDataService()
        self.device = ProjectDevice("AC", ["TE1", "TE2", "TE3", "TE4"],"AC1", "MMM")
        self.device2 = ProjectDevice("AC", ["TE1", "TE2"],"AC2", "MMM")

    def test_device_list_created_empty(self):
        self.assertEqual(self.service.get_device_list(), {})

    def test_device_added_correctly(self):
        self.service.add_device(self.device)
        self.assertEqual(len(self.service.get_device_list()),1)

    def test_remove_device_works(self):
        self.service.add_device(self.device)
        self.service.remove_device("AC1")
        self.assertEqual(len(self.service.get_device_list()),0)

    def test_get_device_with_multiple_devices(self):
        self.service.add_device(self.device)
        self.service.add_device(self.device2)
        self.assertEqual(len(self.service.get_device_list()),2)

    def test_get_points_with_multiple_devices(self):
        self.service.add_device(self.device)
        self.service.add_device(self.device2)
        result = self.service.get_point_list()
        self.assertEqual(len(result["AC1"]),4)
        self.assertEqual(len(result["AC2"]),2)