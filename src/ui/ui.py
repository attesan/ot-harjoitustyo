from tkinter import Tk
from ui.main_window import mainView

class UI:
    def __init__(self, root):
        self.root = root
    
    def start(self):
        self._show_hello_view()

    def _handle_good_bye(self):
        print("goodbye whatever that means")

    def _show_hello_view(self):
        self._current_view = mainView(self.root, self._handle_good_bye)


window = Tk()
window.title("testi")

ui = UI(window)
ui.start()

window.mainloop()