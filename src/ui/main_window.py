from tkinter import ttk, constants, Menu

class mainView:
    def __init__(self, root, handle_good_bye):
        self._root = root
        self._handle_good_bye = handle_good_bye
        self._frame = None
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        top_menu = Menu(self._root)
        dropdown_menu_add = Menu(master=top_menu, tearoff=0)
        dropdown_menu_add.add_command(label="Laite projektiin", command=NotImplemented)
        dropdown_menu_add.add_command(label="Testi", command=NotImplemented)

        dropdown_menu_project = Menu(master=top_menu, tearoff=0)
        dropdown_menu_project.add_command(label="Tallenna", command=NotImplemented)
        dropdown_menu_project.add_command(label="Avaa projekti", command=NotImplemented)
        dropdown_menu_project.add_command(label="Vie CSV", command=NotImplemented)

        dropdown_menu_data = Menu(master=top_menu, tearoff=0)
        dropdown_menu_data.add_command(label="Lisää laite tietokantaan", command=NotImplemented)
        dropdown_menu_data.add_command(label="Muokkaa tietokannan laitetta", command=NotImplemented)

        top_menu.add_cascade(label="Projekti", menu=dropdown_menu_project)
        top_menu.add_cascade(label="Lisää", menu=dropdown_menu_add)
        top_menu.add_cascade(label="Tietokanta", menu=dropdown_menu_data)

        self._root.config(menu=top_menu)

    def destroy(self):
        self._frame.destroy()

    def pack(self):
        self._frame.pack(fill=constants.X)