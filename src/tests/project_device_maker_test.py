import unittest
import os
import sys
from services.project_device_maker import ProjectDeviceMaker
from repository.device_repository import DeviceRepository
from initialize_database import initialize_database
from services.project_data_service import ProjectDataService
from entities.project_device import ProjectDevice

sys.path.insert(0, os.path.abspath(".."))

class TestProjectDeviceMaker(unittest.TestCase):
    def setUp(self):
        self.d = ProjectDeviceMaker()
        self.device = ("model1", "manufacturer1",[("point11","text11","type11"),("point12","text12","type12"),("point13","text13","type13"),("point14","text14","type14")])
        self.d._devices.new_device(self.device[0],self.device[1],self.device[2])

    def test_has_device_repository(self):
        self.assertEqual(self.d._devices.__class__,DeviceRepository().__class__)

    def test_make_device_return_type(self):
        result = self.d.make_project_device("a",1)
        self.assertEqual(result.__class__,ProjectDevice("","","","").__class__)

    def test_make_device_device_points(self):
        result = self.d.make_project_device("a",1)
        self.assertEqual(len(result.get_points()),4)

    def test_make_device_device_points(self):
        result = self.d.make_project_device("a",1)
        self.assertEqual(result.position,"a")