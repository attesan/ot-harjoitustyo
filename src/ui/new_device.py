from tkinter import ttk, constants


class NewDevice:
    # This view lets the user create new devices into the program database. These can then be added to project.
    def __init__(self, root, handle_main_window):
        self._root = root
        self._frame = None
        self._handle_main_window = handle_main_window
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self.device_name = ttk.Label(master=self._frame, text="Laitteen nimi")
        self.device_made_by = ttk.Label(master=self._frame, text="Valmistaja")
        self.device_point_name1 = ttk.Label(master=self._frame, text="Piste 1")
        self.device_point_name2 = ttk.Label(master=self._frame, text="Piste 2")
        self.device_point_name3 = ttk.Label(master=self._frame, text="Piste 3")
        self.device_point_name4 = ttk.Label(master=self._frame, text="Piste 4")

        self.device_name_field = ttk.Entry(master=self._frame)
        self.device_made_by_field = ttk.Entry(master=self._frame)
        self.device_point_name_field1 = ttk.Entry(master=self._frame)
        self.device_point_name_field2 = ttk.Entry(master=self._frame)
        self.device_point_name_field3 = ttk.Entry(master=self._frame)
        self.device_point_name_field4 = ttk.Entry(master=self._frame)

        self.save_button = ttk.Button(master=self._frame, text="Tallenna")
        self.close_button = ttk.Button(
            master=self._frame, text="Peruuta", command=self._handle_main_window)

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

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)
