from database_handler import DatabaseHandler
from filehandler import FileHandler


class Controller:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.filehandler = None

    # def setup(self):
    #     """Create needed objects for controller"""
    #     file = FileHandler.get_file_name()
    def set_file(self, filename):
        """Set the file that will create the filehandler object"""
        self.filehandler = FileHandler(filename)
        self.filehandler.set_file_type()

    def read(self):
        """Read selected file"""
        self.filehandler.read()

    # def run(self):
    #     a = FileHandler.get_file_name()
    #     aclass = FileHandler(a)
    #     while aclass.file_exist() is False:
    #         print("File exists:", aclass.file_exist())
    #         a = FileHandler.get_file_name()
    #         aclass = FileHandler(a)
    #     aclass.set_file_type()
    #     aclass.read()

