from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database

def main():
    window = Tk()
    window.title("RAU laite ja pistesovellus")

    initialize_database()

    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()