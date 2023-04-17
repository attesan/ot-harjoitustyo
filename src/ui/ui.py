from tkinter import Tk
from ui.main_window import MainView
from ui.new_device import NewDevice
from ui.edit_device import EditDevice

class UI:
    # This class handles the UI
    def __init__(self, root):
        self.root = root
        self._current_view = None

    def start(self):
        self._show_main_window()

    def _hide_view(self):
        if self._current_view:
            self._current_view.destroy()
        self._current_view = None

    # Handles for different window transitions
    def _handle_main_window(self):
        self._show_main_window()

    def _handle_new_device(self):
        self._show_new_device()

    def _handle_edit_device(self):
        self._show_edit_device()

    # Methods for showing different windows
    def _show_main_window(self):
        self._hide_view()
        self._current_view = MainView(self.root, self._handle_new_device, self._handle_edit_device)
        self._current_view.pack()

    def _show_new_device(self):
        self._hide_view()
        self._current_view = NewDevice(self.root, self._handle_main_window)
        self._current_view.pack()

    def _show_edit_device(self):
        self._hide_view()
        self._current_view = EditDevice(self.root, self._handle_main_window)
        self._current_view.pack()
