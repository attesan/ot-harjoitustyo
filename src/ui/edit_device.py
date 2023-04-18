import os
import sys
from repository.device_repository import DeviceRepository
from tkinter import ttk, constants, END

sys.path.insert(0, os.path.abspath(".."))

class EditDevice:
    # This class lets the user check what devices are added in the program and edit them.
    def __init__(self, root, handle_main_window):
        self._root = root
        self._frame = None
        self._handle_main_window = handle_main_window
        self._devices = DeviceRepository()
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        # Labels
        self._device_list_label = ttk.Label(master=self._frame, text="Tietokannan laitteet")
        self._device_data_label = ttk.Label(master=self._frame, text="Laitteen tiedot")
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

        # Lists
        self._device_list = ttk.Treeview(
            master=self._frame, 
            columns=(0,1,2,3,4,5), 
            show="headings", 
            selectmode="browse")
        self._device_list.heading(0, text="Laite")
        self._device_list.heading(1, text="Valmistaja")
        self._device_list.heading(2, text="Piste 1")
        self._device_list.heading(3, text="Piste 2")
        self._device_list.heading(4, text="Piste 3")
        self._device_list.heading(5, text="Piste 4")
        self._device_list.bind("<<TreeviewSelect>>",self.populate_fields_with_selected_device_data)

        # Buttons
        self.close_button = ttk.Button(
            master=self._frame, text="Peruuta", command=self._handle_main_window)
        self.save_button = ttk.Button(
            master=self._frame, text="Tallenna")

        # Grid for all view objects
        self._device_list_label.grid(row=0, column=0)
        self._device_data_label.grid(row=0, column=1)

        self._device_list.grid(row=1, column=0)

        self.device_name.grid(row=0, column=1)
        self.device_name_field.grid(row=0, column=2)
        self.device_made_by.grid(row=1, column=1)
        self.device_made_by_field.grid(row=1, column=2)
        self.device_point_name1.grid(row=2, column=1)
        self.device_point_name_field1.grid(row=2, column=2)
        self.device_point_name2.grid(row=3, column=1)
        self.device_point_name_field2.grid(row=3, column=2)
        self.device_point_name3.grid(row=4, column=1)
        self.device_point_name_field3.grid(row=4, column=2)
        self.device_point_name4.grid(row=5, column=1)
        self.device_point_name_field4.grid(row=5, column=2)

        self.save_button.grid(row=6, column=0)
        self.close_button.grid(row=6, column=1)

        self.get_devices()

    # This method inserts device and point data from database search to device_list
    def get_devices(self):
        # Get device data
        devices = self._devices.find_all_devices()

        # Process every device
        for row in devices: 
            # Get point data
            points = self.get_point_data(row[0])

            # Insert data into device_list
            data = list(row) + points[:4]
            self._device_list.insert("","end",values=data)
    
    # Get point data and return it as list for now because other point data is not implemented yet
    def get_point_data(self, device):
        # Get point data from database
        points = self._devices.find_device_points(device)

        # Filter point names from result
        data = []
        for row in points:
            data.append(row[0])
        return data
    
    # Get data from selected device
    def populate_fields_with_selected_device_data(self, x):
        self.clear_fields()

        device = self._device_list.focus()
        device = self._device_list.item(device)
        data = device["values"]

        self.device_name_field.insert(0,data[0])
        self.device_made_by_field.insert(0,data[1])
        self.device_point_name_field1.insert(0,data[2])
        self.device_point_name_field2.insert(0,data[3])
        self.device_point_name_field3.insert(0,data[4])
        self.device_point_name_field4.insert(0,data[5])
    
    # Clear old device data from fields
    def clear_fields(self):
        self.device_name_field.delete(0, END)
        self.device_made_by_field.delete(0, END)
        self.device_point_name_field1.delete(0, END)
        self.device_point_name_field2.delete(0, END)
        self.device_point_name_field3.delete(0, END)
        self.device_point_name_field4.delete(0, END)

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
