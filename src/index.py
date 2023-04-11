import os
import sys
from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database

sys.path.insert(0, os.path.abspath(".."))

def main():
    window = Tk()
    window.title("RAU laite ja pistesovellus")

    initialize_database()

    main_ui = UI(window)
    main_ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()
