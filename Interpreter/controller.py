<<<<<<< HEAD
from database_handler import DatabaseHandler
from filehandler import FileHandler


class Controller:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.filehandler = None

    def set_file(self, filename):
        """Set the file that will create the filehandler object"""
        self.filehandler = FileHandler(filename)
        self.filehandler.set_file_type()

    def read(self):
        """Read selected file"""
        self.filehandler.read()

    def set_local(self, name):
        """
        Set the local database with a specified name
        :param name:
        :return:
        """
        pass

    def local_update(self, dictionary):
        """
        Update the local dictionary
        :param dictionary: Contains validated and pickled data
        :return: Void: Will input the dictionary into the local database
        """
        # self.db_handler.
        pass


=======
from database_handler import DatabaseHandler
from filehandler import FileHandler


class Controller:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.filehandler = None

    def set_file(self, filename):
        """Set the file that will create the filehandler object"""
        self.filehandler = FileHandler(filename)
        self.filehandler.set_file_type()

    def read(self):
        """Read selected file"""
        # if self.filehandler.file_exist():
        self.filehandler.read()

    def set_local(self, name):
        """
        Set the local database with a specified name
        :param name:
        :return:
        """
        pass

    def local_update(self, dictionary):
        """
        Update the local dictionary
        :param dictionary: Contains validated and pickled data
        :return: Void: Will input the dictionary into the local database
        """
        # self.db_handler.
        pass


>>>>>>> 6540e0402541687358a943f73273ca0ddaad4381
