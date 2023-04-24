import os
import sys
from tkinter import ttk, constants
from repository.device_repository import DeviceRepository

sys.path.insert(0, os.path.abspath(".."))

class AddProjectDevice:
    # This class lets user add devices into project. Added devices are shown in main view. The devices are added as device -objects.
    # View has fields for project specific data, such as device position: apparatus/machine the device is a logical part of.
    # For example, Temperature sensor "TE1" that is part of Air conditioner "AC1". This information is shown in main view
    # and is used to compose the full point name for the device.
    def __init__(self, root, handle_main_window):
        self._root = root
        self._frame = None
        self._handle_main_window = handle_main_window
        self._devices = DeviceRepository()
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Labels
        self._devices_label = ttk.Label(master=self._frame, text="Laitteet")
        self._device_position_label = ttk.Label(master=self._frame, text="Positio")

        # List
        self._device_list = ttk.Treeview(
            master=self._frame,
            columns=(0,1),
            show="headings",
            selectmode="browse")
        self._device_list.heading(0, text="Malli")
        self._device_list.heading(1, text="Valmistaja")

        # Fields
        self._device_position = ttk.Entry(master=self._frame)

        # Buttons
        self._add_to_project_button = ttk.Button(
            master=self._frame, 
            text="Lisää projektiin",
            command=NotImplemented)
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

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
