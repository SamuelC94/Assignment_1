from database_handler import DatabaseHandler
from filehandler import FileHandler
from os import path
from chart import Graph
import doctest


class Controller:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.filehandler = None
        self.graph = None

    def set_file(self, filename):
        """Set the file that will create the filehandler object"""
        if path.exists(filename):
            self.filehandler = FileHandler(filename)
            self.filehandler.set_file_type()
            return True
        else:
            return False

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

    def set_graph(self, dictionary, type, filename):
        self.graph = Graph
        self.graph.set_data(dictionary, type, filename)


# Controller shouldn't run doctests???
# if __name__ == "__main__":
#     c = Controller()
#     doctest.testmod()

