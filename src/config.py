import os
from dotenv import load_dotenv

directory_name = os.path.dirname(__file__)

""" Contains configuration information of program.
Placeholder for config file. Will be added if there is enough time.
"""

try:
    load_dotenv(dotenv_path=os.path.join(directory_name, "..", ".env"))
except FileNotFoundError:
    pass

DEVICES_FILENAME = os.getenv("DEVICES_FILENAME") or "Devices.dp"
