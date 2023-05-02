import unittest
import os
import sys
from entities.project_device import ProjectDevice

sys.path.insert(0, os.path.abspath(".."))

class TestProjectDevice(unittest.TestCase):
    def setUp(self):
        self.device = ProjectDevice("AC", ["TE1", "TE2", "TE3", "TE4"], "AC1")
        self.device2 = ProjectDevice("AC", ["TE1"], "AC1", ".")

    def test_device_points_created_correctly(self):
        self.assertEqual(len(self.device.points), 4)

    def test_device_point_created_correctly(self):
        self.assertEqual(len(self.device2.points), 1)

    def test_type_getter_works(self):
        self.assertEqual(self.device.type, "AC")

    def test_points_getter_works(self):
        self.assertEqual(len(self.device.points), 4)

    def test_position_getter_works(self):
        self.assertEqual(self.device.position, "AC1")

    def test_position_setter_works(self):
        self.device.position = "TK"
        self.assertEqual(self.device.position, "TK")

    def test_return_value_data_check(self):
        result = self.device._ProjectDevice__check_valid("Aa1")
        self.assertEqual(result, True)

    def test_return_value_separator_included_data_check(self):
        result = self.device._ProjectDevice__check_valid("_Aa1")
        self.assertEqual(result, False)
    
    def test_return_value_custom_separator_included_data_check(self):
        result = self.device2._ProjectDevice__check_valid(".Aa1")
        self.assertEqual(result, False)

    def test_return_value_invalid_data_check(self):
        result = self.device._ProjectDevice__check_valid("`/§½€£<>")
        self.assertEqual(result, False)

    def test_position_setter_invalid_input_detected(self):
        self.device.position = "`/§½€£<>"
        self.assertEqual(self.device.position, "AC1")

    def test_get_point_data(self):
        self.assertEqual(len(self.device.get_points()), 4)
