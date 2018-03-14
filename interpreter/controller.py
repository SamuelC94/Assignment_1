# Interpreter/controller.py
from database_handler import DatabaseHandler
from filehandler import FileHandler
from os import path
from chart import Graph
import doctest


# Will need to connect the filehandler/validator
# Dictionary as a whole can get passed to the chart
# select keys for data
# Then the x/y axis and title
# Then draw

# need to add commands in prompt and controller to use the functions
# When validator/filehandler is sorted then I can quickly sort the database handler

# need to create tests and add more doctests, examples in chart
# More exception handling
# To show 'robustness' then we just need to prevent all errors in the shell? or will he want us to use as a package?

class Controller:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.data = None
        self.filehandler = None
        self.graph = None

    def load(self, filename):
        """
        Set the file that will create the filehandler object
        """
        if path.exists(filename):
            self.filehandler = FileHandler(filename)
            self.filehandler.set_file_type()
            return True
        else:
            return False

    def validate(self):
        """
        Read selected file
        """
        # James' changes (13/03)
        result = self.filehandler.read()
        self.data = result
        print(result)

    def print_dict(self, data):
        # Tabulate package to print out a nice looking table in the console
        pass

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

    def set_graph(self, graph_type, filename):
        print(graph_type)
        print(filename)
        self.graph = Graph()
        data = self.data
        self.graph.set_data(data, graph_type, filename)

    def set_criteria(self, criteria_1, criteria_2):
        self.graph.set_criteria(criteria_1, criteria_2)

    def set_keys(self, key_1, key_2):
        self.graph.set_keys(key_1, key_2)

    def draw(self, x, y, title):
        self.graph.draw(x, y, title)


# Controller shouldn't run doctests???
# if __name__ == "__main__":
#     c = Controller()
#     doctest.testmod()