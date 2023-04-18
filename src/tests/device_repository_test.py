import unittest
import os
import sys
from repository.device_repository import DeviceRepository

sys.path.insert(0, os.path.abspath(".."))

class TestDeviceRepository(unittest.TestCase):
    def setUp(self):
        self.d = DeviceRepository()
        self.d.delete_all()

        # Note to self, create class for device handling!
        # Note to self, add tests for points and device data!
        self.device1 = ("model1", "manufacturer1",[("point11","text11","type11"),("point12","text12","type12"),("point13","text13","type13"),("point14","text14","type14")])
        self.device2 = ("model2", "manufacturer2",[("point21","text21","type21")])

    def test_add_device(self):
        self.d.new_device(self.device1[0],self.device1[1],self.device1[2])
        result = self.d.find_all_devices()

        self.assertEqual(len(result),1)
    
    def test_add_multiple_devices(self):
        self.d.new_device(self.device1[0],self.device1[1],self.device1[2])
        self.d.new_device(self.device2[0],self.device2[1],self.device2[2])
        result = self.d.find_all_devices()

        self.assertEqual(len(result),2)

    def test_search_by_device_model_one_device(self):
        self.d.new_device(self.device1[0],self.device1[1],self.device1[2])
        result = self.d.search_by_model(self.device1[0])

        self.assertEqual(result[1], self.device1[0])

    def test_search_by_device_model_multiple_devices_search_first(self):
        self.d.new_device(self.device1[0],self.device1[1],self.device1[2])
        self.d.new_device(self.device2[0],self.device2[1],self.device2[2])
        result = self.d.search_by_model(self.device1[0])
        
        self.assertEqual(result[1], self.device1[0])

    def test_search_by_device_model_multiple_devices_search_last(self):
        self.d.new_device(self.device1[0],self.device1[1],self.device1[2])
        self.d.new_device(self.device2[0],self.device2[1],self.device2[2])
        result = self.d.search_by_model(self.device2[0])
        
        self.assertEqual(result[1], self.device2[0])

    def test_delete_all_works(self):
        self.d.new_device(self.device1[0],self.device1[1],self.device1[2])
        self.d.new_device(self.device2[0],self.device2[1],self.device2[2])
        self.d.delete_all()
        result = self.d.find_all_devices()
        
        self.assertEqual(len(result), 0)

    def test_points_added_correctly_none(self):
        self.d.new_device(self.device2[0],self.device2[1],[])
        result = self.d.find_device_points("model1")

        self.assertEqual(len(result), 0)

    def test_points_added_correctly_one(self):
        self.d.new_device(self.device2[0],self.device2[1],self.device2[2])
        result = self.d.find_device_points("model2")

        self.assertEqual(len(result), 1)

    def test_points_added_correctly_many(self):
        self.d.new_device(self.device1[0],self.device1[1],self.device1[2])
        result = self.d.find_device_points("model1")

        self.assertEqual(len(result), 4)
