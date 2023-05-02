from tkinter import ttk, constants, Menu

class MainView:
    """Primary view of the program. User can access other views from this view.
    User can get to other windows from here and view project data.

    Attributes: 
        _root: root for view objects
        _frame: Current frame, initally None
        _handle_add_project_device: reference for window transition to add project device window.
        _handle_new_device: reference for window transition to new device window.
        _handle_edit_device: reference for window transition to edit device window.
        _project_data_service: reference to project data service for getting project data.
    """
    def __init__(self, root, handle_add_project_device, handle_new_device, handle_edit_device, project_data_service):
        """Constructor for class. Sets initial parameters and initializes the main window. 
        
        Args:
            root: root for view objects
            handle_add_project_device: reference for window transition to add project device window.
            handle_new_device: reference for window transition to new device window.
            handle_edit_device: reference for window transition to edit device window.
            project_data_service: reference to project data service for getting project data.
        """
        self._root = root
        self._frame = None
        self._handle_add_project_device = handle_add_project_device
        self._handle_new_device = handle_new_device
        self._handle_edit_device = handle_edit_device
        self.project_data_service = project_data_service
        self._initialize()

    def _initialize(self):
        """For initializing the main window and showing project data.
        """
        self._frame = ttk.Frame(master=self._root)

        # Top edge menu bar that contains dropdown menus
        self.top_menu = Menu(self._frame)

        # These are the dropdown menus visible on top_menu
        self.dropdown_menu_add = Menu(master=self.top_menu, tearoff=0)
        self.dropdown_menu_add.add_command(
            label="Laite projektiin", 
            command=self._handle_add_project_device)
        self.dropdown_menu_add.add_command(
            label="Testi", 
            command=NotImplemented)

        self.dropdown_menu_project = Menu(master=self.top_menu, tearoff=0)
        self.dropdown_menu_project.add_command(
            label="Tallenna", 
            command=NotImplemented)
        self.dropdown_menu_project.add_command(
            label="Avaa projekti", 
            command=NotImplemented)
        self.dropdown_menu_project.add_command(
            label="Vie CSV", 
            command=NotImplemented)

        self.dropdown_menu_data = Menu(master=self.top_menu, tearoff=0)
        self.dropdown_menu_data.add_command(
            label="Lisää laite tietokantaan", 
            command=self._handle_new_device)
        self.dropdown_menu_data.add_command(
            label="Muokkaa tietokannan laitetta", 
            command=self._handle_edit_device)

        # Add different dropdown menus to top menu bar
        self.top_menu.add_cascade(
            label="Projekti", 
            menu=self.dropdown_menu_project)
        self.top_menu.add_cascade(
            label="Lisää", 
            menu=self.dropdown_menu_add)
        self.top_menu.add_cascade(
            label="Tietokanta", 
            menu=self.dropdown_menu_data)

        # Labels
        self.devices_label = ttk.Label(master=self._frame, text="Laitteet")
        self.points_label = ttk.Label(master=self._frame, text="Pisteet")

        # Lists for points and devices
        self.devices_treeview = ttk.Treeview(
            master=self._frame,
            columns=(0,1,2),
            show="headings")
        self.devices_treeview.heading(0,text="Positio")
        self.devices_treeview.heading(1,text="Malli")
        self.devices_treeview.heading(2,text="Valmistaja")

        self.points_treeview = ttk.Treeview(
            master=self._frame,
            columns=(0,1,2,3),
            show="headings")
        self.points_treeview.heading(0,text="Laitepositio")
        self.points_treeview.heading(1,text="Piste")
        self.points_treeview.heading(2,text="Tyyppi")
        self.points_treeview.heading(3,text="Pistetunnus")

        # Grid for view objects
        self.points_label.grid(row=0, column=0)
        self.points_treeview.grid(row=1, column=0)
        self.devices_label.grid(row=0, column=1)
        self.devices_treeview.grid(row=1, column=1)

        self._root.config(menu=self.top_menu)

        #self.populate_list() to buggy to include right now.

    def populate_list(self):
        """Get device and point data from project data manager and add it to points and devices -lists.
        """
        devices = self.project_data_service.get_device_list()
        for device_position, device in devices:
            self.devices_treeview.insert("","end",values=(device_position,device.model,device.manufacturer))

        points = self.project_data_service.get_point_list()
        for device_position, device_points in points:
            for point in device_points:
                self.points_treeview.insert("","end",values=(device_position, point.point_position, self.point_type, self.point_name))

    def destroy(self):
        """For destroying the current view frame.
        """
        self._frame.destroy()

    def pack(self):
        """For packing the view.
        """
        self._frame.pack(fill=constants.X)
