import os
import sys
from repository.device_repository import DeviceRepository
from tkinter import ttk, constants
from services.project_data_service import ProjectDataService

sys.path.insert(0, os.path.abspath(".."))

class NewDevice:
    # This view lets the user create new devices into the program database. These can then be added to project.
    # Currently only contains basic data like manufacturer and few points for every device.
    def __init__(self, root, handle_main_window):
        self._root = root
        self._frame = None
        self._handle_main_window = handle_main_window
        self._devices = DeviceRepository()
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Labels for fields
        self.device_name = ttk.Label(master=self._frame, text="Laitteen nimi")
        self.device_made_by = ttk.Label(master=self._frame, text="Valmistaja")
        self.device_point_name1 = ttk.Label(master=self._frame, text="Piste 1")
        self.device_point_name2 = ttk.Label(master=self._frame, text="Piste 2")
        self.device_point_name3 = ttk.Label(master=self._frame, text="Piste 3")
        self.device_point_name4 = ttk.Label(master=self._frame, text="Piste 4")

        # Fields
        self.device_name_field = ttk.Entry(master=self._frame)
        self.device_made_by_field = ttk.Entry(master=self._frame)
        self.device_point_name_field1 = ttk.Entry(master=self._frame)
        self.device_point_name_field2 = ttk.Entry(master=self._frame)
        self.device_point_name_field3 = ttk.Entry(master=self._frame)
        self.device_point_name_field4 = ttk.Entry(master=self._frame)

        # Buttons
        self.save_button = ttk.Button(master=self._frame, text="Tallenna", 
            command=self.save_new_device)
        self.close_button = ttk.Button(
            master=self._frame, text="Peruuta", 
            command=self._handle_main_window)

        # Grid for all view objects.
        self.device_name.grid()
        self.device_name_field.grid(row=0, column=1)
        self.device_made_by.grid(row=0, column=2)
        self.device_made_by_field.grid(row=0, column=3)
        self.device_point_name1.grid(row=1, column=0)
        self.device_point_name_field1.grid(row=1, column=1)
        self.device_point_name2.grid(row=2, column=0)
        self.device_point_name_field2.grid(row=2, column=1)
        self.device_point_name3.grid(row=3, column=0)
        self.device_point_name_field3.grid(row=3, column=1)
        self.device_point_name4.grid(row=4, column=0)
        self.device_point_name_field4.grid(row=4, column=1)
        self.save_button.grid(row=5, column=0)
        self.close_button.grid(row=5, column=1)

    def save_new_device(self):
        name = self.device_name_field.get()
        manufacturer = self.device_made_by_field.get()
        point1 = self.device_point_name_field1.get()
        point2 = self.device_point_name_field2.get()
        point3 = self.device_point_name_field3.get()
        point4 = self.device_point_name_field4.get()

        # Check that at least minimum information is given.
        if name == "" or point1 == "" :
            return
        self._devices.new_device(name, manufacturer, [(point1,),(point2,),(point3,),(point4,)])

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
