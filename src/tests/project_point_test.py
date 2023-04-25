import unittest
import os
import sys
from entities.project_point import ProjectPoint

sys.path.insert(0, os.path.abspath(".."))

class TestProjectPoint(unittest.TestCase):
    def setUp(self):
        self.point = ProjectPoint("AC1","TE1","AI")
        self.point2 = ProjectPoint("AC1","TE1","AI",".")

    # Default parameter tests
    def test_point_device_position_created_correctly(self):
        self.assertEqual(self.point.device_position, "AC1")

    def test_point_position_created_correctly(self):
        self.assertEqual(self.point.point_position, "TE1")

    def test_point_type_created_correctly(self):
        self.assertEqual(self.point.point_type,"AI")

    def test_point_initialization_point_name_composed_correctly(self):
        self.assertEqual(self.point.point_name, "AC1_TE1_AI")

    def test_change_point_device(self):
        self.point.device_position = "AC2"
        self.assertEqual(self.point.device_position, "AC2")

    def test_change_point_position(self):
        self.point.point_position = "TE2"
        self.assertEqual(self.point.point_position, "TE2")
    
    def test_change_point_type(self):
        self.point.point_type = "DI"
        self.assertEqual(self.point.point_type, "DI")

    def test_change_point_device_name_updates(self):
        self.point.device_position = "AC2"
        self.assertEqual(self.point.point_name, "AC2_TE1_AI")

    def test_change_point_position_name_updates(self):
        self.point.point_position = "TE2"
        self.assertEqual(self.point.point_name, "AC1_TE2_AI")
    
    def test_change_point_type_name_updates(self):
        self.point.point_type = "DI"
        self.assertEqual(self.point.point_name, "AC1_TE1_DI")

    # Custom separator tests
    def test_custom_separator_point_device_position_created_correctly(self):
        self.assertEqual(self.point2.device_position, "AC1")

    def test_custom_separator_point_position_created_correctly(self):
        self.assertEqual(self.point2.point_position, "TE1")

    def test_custom_separator_point_type_created_correctly(self):
        self.assertEqual(self.point2.point_type,"AI")

    def test_custom_separator_point_creation_point_name_composed_correctly(self):
        self.assertEqual(self.point2.point_name, "AC1.TE1.AI")

    def test_custom_separator_change_point_device(self):
        self.point2.device_position = "AC2"
        self.assertEqual(self.point2.device_position, "AC2")

    def test_custom_separator_change_point_position(self):
        self.point2.point_position = "TE2"
        self.assertEqual(self.point2.point_position, "TE2")
    
    def test_custom_separator_change_point_type(self):
        self.point2.point_type = "DI"
        self.assertEqual(self.point2.point_type, "DI")

    def test_custom_separator_change_point_device_name_updates(self):
        self.point2.device_position = "AC2"
        self.assertEqual(self.point2.point_name, "AC2.TE1.AI")

    def test_custom_separator_change_point_position_name_updates(self):
        self.point2.point_position = "TE2"
        self.assertEqual(self.point2.point_name, "AC1.TE2.AI")
    
    def test_custom_separator_change_point_type_name_updates(self):
        self.point2.point_type = "DI"
        self.assertEqual(self.point2.point_name, "AC1.TE1.DI")

    # Valid data check return value tests
    def test_return_value_data_check(self):
        result = self.point._ProjectPoint__check_valid("AC1")
        self.assertEqual(result,True)

    # Invalid data return value tests
    def test_return_value_invalid_character_data_check(self):
        result = self.point._ProjectPoint__check_valid("_AC1")
        self.assertEqual(result,False)

    def test_return_value_separator_included_data_check(self):
        result = self.point._ProjectPoint__check_valid("AC*")
        self.assertEqual(result,False)

    def test_invalid_character_device_position_no_name_update(self):
        self.point.device_position = "AC*"
        self.assertEqual(self.point.point_name, "AC1_TE1_AI")

    def test_invalid_character_point_position_no_name_update(self):
        self.point.point_position = "TE*"
        self.assertEqual(self.point.point_name, "AC1_TE1_AI")

    def test_invalid_character_point_type_no_name_update(self):
        self.point.point_type = "AI*"
        self.assertEqual(self.point.point_name, "AC1_TE1_AI")

    def test_separator_included_in_device_position_no_name_update(self):
        self.point.device_position = "AC_"
        self.assertEqual(self.point.point_name, "AC1_TE1_AI")

    def test_separator_included_in_point_position_no_name_update(self):
        self.point.point_position = "TE1_"
        self.assertEqual(self.point.point_name, "AC1_TE1_AI")

    def test_separator_included_in_point_type_no_name_update(self):
        self.point.point_type = "AI_"
        self.assertEqual(self.point.point_name, "AC1_TE1_AI")

    def test_invalid_character_device_position_no_point_data_update(self):
        self.point.device_position = "AC*"
        self.assertEqual(self.point.device_position, "AC1")

    def test_invalid_character_point_position_no_point_data_update(self):
        self.point.point_position = "TE*"
        self.assertEqual(self.point.point_position, "TE1")

    def test_invalid_character_point_type_no_point_data_update(self):
        self.point.point_type = "AI*"
        self.assertEqual(self.point.point_type, "AI")

    def test_separator_included_in_device_position_no_point_data_update(self):
        self.point.device_position = "AC_"
        self.assertEqual(self.point.device_position, "AC1")

    def test_separator_included_in_point_position_no_point_data_update(self):
        self.point.point_position = "TE1_"
        self.assertEqual(self.point.point_position, "TE1")

    def test_separator_included_in_point_type_no_point_data_update(self):
        self.point.point_type = "AI_"
        self.assertEqual(self.point.point_type, "AI")
