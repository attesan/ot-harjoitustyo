import os
import sys
from repository.device_repository import DeviceRepository
from tkinter import ttk, constants

sys.path.insert(0, os.path.abspath(".."))

class EditDevice:
    # This view lets the user check what devices are added in the program and edit them.
    def __init__(self, root, handle_main_window):
        self._root = root
        self._frame = None
        self._handle_main_window = handle_main_window
        self._devices = DeviceRepository()
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._label = ttk.Label(master=self._root, text="Tietokannan laitteet")

        self._device_list = ttk.Treeview(master=self._root)

        self._close_button = ttk.Button(
            master=self._root, text="Peruuta", command=self._handle_main_window)
        
        # Grid for all view objects
        self._label.grid(row=0, column=0)
        self._device_list.grid(row=1, column=0)
        self._close_button.grid(row=3, column=0)

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
