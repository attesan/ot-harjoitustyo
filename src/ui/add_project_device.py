import os
import sys
from tkinter import ttk, constants
from repository.device_repository import DeviceRepository
from services.project_device_maker import ProjectDeviceMaker

sys.path.insert(0, os.path.abspath(".."))

class AddProjectDevice:
    # This class lets user add devices into project. Added devices are shown in main view. The devices are added as device -objects.
    # View has fields for project specific data, such as device position: apparatus/machine the device is a logical part of.
    # For example, Temperature sensor "TE1" that is part of Air conditioner "AC1". This information is shown in main view
    # and is used to compose the full point name for the device.
    def __init__(self, root, handle_main_window, project_data_service):
        self._root = root
        self._frame = None
        self._handle_main_window = handle_main_window
        self._devices = DeviceRepository()
        self.project_data_service = project_data_service
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Labels
        self._devices_label = ttk.Label(master=self._frame, text="Laitteet")
        self._device_position_label = ttk.Label(master=self._frame, text="Positio")

        # List
        self._device_list = ttk.Treeview(
            master=self._frame,
            columns=(0,1,2),
            show="headings",
            selectmode="browse")
        self._device_list.heading(0, text="Id")
        self._device_list.heading(1, text="Malli")
        self._device_list.heading(2, text="Valmistaja")

        # Fields
        self._device_position = ttk.Entry(master=self._frame)

        # Buttons
        self._add_to_project_button = ttk.Button(
            master=self._frame, 
            text="Lisää projektiin",
            command=self.add_to_project)
        self._cancel_button = ttk.Button(
            master=self._frame, 
            text="Peruuta",
            command=self._handle_main_window)
    
        # Grid for all view objects
        self._devices_label.grid(row=0,column=0)
        self._device_position_label.grid(row=0,column=1)
        self._device_list.grid(row=1, column=0)
        self._device_position.grid(row=1,column=1)
        self._add_to_project_button.grid(row=2, column=0)
        self._cancel_button.grid(row=2,column=1)

        #self.get_devices() to buggy to include right now.

    # This method inserts device and point data from database search to device_list.
    def get_devices(self):
        # Get device data
        devices = self._devices.find_all_devices()

        # Insert data into device_list
        for row in devices: 
            data = list(row)
            self._device_list.insert("","end",values=data)

    # This method is used to add devices into the project.
    def add_to_project(self):
        # Get values of selected item from list and device position.
        device = self._device_list.focus()
        device = self._device_list.item(device)
        data = device["values"]
        # Make sure something is selected.
        if data == "":
            return

        device_position = self._device_position.get()

        # Find device and device point data by device id and create a project_device -object.
        device_maker = ProjectDeviceMaker()
        new_project_device = device_maker.make_project_device(device_position,data[0])
        
        # Add project_device to project data manager.
        self.project_data_service.add_device(new_project_device)

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
