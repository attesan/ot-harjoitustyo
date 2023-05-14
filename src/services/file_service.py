import os
import sys
import csv

sys.path.insert(0, os.path.abspath(".."))

class FileService:
    """This class is responsible for saving project data to file.
    Can be expanded to handle loading data from file.

    Attributes:
        project_data_service: a project_data_service -object that contains project data to be saved
    """

    def __init__(self,project_data_service):
        """Constructor for FileService.
        
        Attributes: 
            _project_data_service: reference to project_data_service -object to be saved"""
        self._project_data_service = project_data_service

    def save_to_csv(self, filename:str):
        """Save project data in csv form supported by excel.
        
        Args:
            filename: name for file to be used.
            
        Return:
            True if successful.
            False if not successful.
        """

        name = filename.split("/")
        if self._check_file_name(name[-1]) is False:
            return False

        data = self._project_data_service.get_csv()
        print("DATA:", data)

        try:
            with open(filename, "w") as file: # pylint: disable=unspecified-encoding
                writer = csv.writer(file, dialect="excel",delimiter=",")
                writer.writerows(data)
                file.close()
            return True
        except: # pylint: disable=bare-except
            return False

    def _check_file_name(self, filename:str):
        """Check given name so it only contains characters that are widely allowed in different
        operating systems.
        
        Args:
            filename: string that is checked.
        
        Return:
            True if filename only has allowed characters.
            False if any character in filename is not allowed.
        """

        allowed = "qQwWeErRtTyYuUiIoOpPåÅaAsSdDfFgGhHjJkKlLöÖäÄzZxXcCvVbBnNmM_ 1234567890."
        for char in filename :
            if char not in allowed:
                return False
        return True
