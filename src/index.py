import os
import sys
from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database
from services.project_data_service import ProjectDataService

sys.path.insert(0, os.path.abspath(".."))

def main():
    """For initializing the program. Has main loop. Creates project_data_Service.
    """
    window = Tk()
    window.title("RAU laite ja pistesovellus")

    initialize_database()
    project_data_service = ProjectDataService()

    main_ui = UI(window, project_data_service)
    main_ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
