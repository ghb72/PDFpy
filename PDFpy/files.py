import os
from os import scandir, getcwd

class FileManager:
    @staticmethod
    def list_files(path=getcwd()) -> list:
        """
        Returns a list of all file names in the specified directory.
        """
        return [arch.name for arch in scandir(path) if arch.is_file()]

    @staticmethod
    def get_current_path() -> None:
        """
        Prints the path of the current working directory.
        """
        print(os.getcwd())
