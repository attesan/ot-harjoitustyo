from tkinter import Tk
from ui.main_window import MainView
from ui.add_project_device import AddProjectDevice
from ui.new_device import NewDevice
from ui.edit_device import EditDevice

class UI:
    """This class handles transitions between different windows.
    
    Attributes: 
        root: root object for view
        _current_view: 
    """
    def __init__(self, root, project_data_service):
        self.root = root
        self._current_view = None
        self.project_data_service = project_data_service

    def start(self):
        """For initially showing main window.
        """
        self._show_main_window()

    def _hide_view(self):
        """For hiding current view.
        """
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    def _handle_main_window(self):
        """For handling transition to main window.
        """
        self._show_main_window()

    def _handle_add_project_device(self):
        """For handling transition to add project device window.
        """
        self._show_add_project_device()

    def _handle_new_device(self):
        """For handling transition to new device window.
        """
        self._show_new_device()

    def _handle_edit_device(self):
        """For handling transition to edit device window.
        """
        self._show_edit_device()

    def _show_main_window(self):
        """For showing main window.
        """
        self._hide_view()
        self._current_view = MainView(self.root, self._handle_add_project_device, self._handle_new_device, self._handle_edit_device, self.project_data_service)
        self._current_view.pack()

    def _show_add_project_device(self):
        """For showing add project device window.
        """
        self._hide_view()
        self._current_view = AddProjectDevice(self.root, self._handle_main_window, self.project_data_service)
        self._current_view.pack()

    def _show_new_device(self):
        """For showing new device window.
        """
        self._hide_view()
        self._current_view = NewDevice(self.root, self._handle_main_window)
        self._current_view.pack()

    def _show_edit_device(self):
        """For showing edit device window.
        """
        self._hide_view()
        self._current_view = EditDevice(self.root, self._handle_main_window)
        self._current_view.pack()
