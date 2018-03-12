from database_handler import DatabaseHandler
from filehandler import FileHandler
from os import path
from chart import Graph


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
    # Wesley ##################################################fix doctest
    def search_key_value(self, dictionary, key, statistic):
        """
        This will search through the given dictionary and return each employee that matches the criteria
        e.g. return a dictionary with all people where their gender is male
        :param dictionary: the data that will be used
        :param key: the key value in the dictionary you would like to search
        :param statistic: the set value you would like to search
        :return:
        >>> search_key_value({0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}, 1: {"IhD": "A2f3", "Gender": "Female", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}}, "Gender", "Male")
        {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal","salary": 20, "Birthday": "24/06/1995"}
        """
        data = {record[0]: record[1] for record in dictionary.items() if record[1][key] == statistic}
        print(data)


    def set_graph(self, dictionary, type, filename):
        self.graph = Graph
        self.graph.set_data(dictionary, type, filename)


a = Controller()
# b = {{"id": 1, "ad": 2, "ifd": 4, "agd": 5, "ihd": 6, "ajd": 7},
#      {"id": 1, "ad": 2, "ifd": 4, "agd": 5, "ihd": 6, "ajd": 7},
#      {"id": 1, "ad": 2, "ifd": 4, "agd": 5, "ihd": 6, "ajd": 7},
#      {"id": 1, "ad": 2, "ifd": 4, "agd": 5, "ihd": 6, "ajd": 7},
#      {"id": 1, "ad": 2, "ifd": 4, "agd": 5, "ihd": 6, "ajd": 7},
#      {"id": 1, "ad": 2, "ifd": 4, "agd": 5, "ihd": 6, "ajd": 7},
#      {"id": 1, "ad": 2, "ifd": 4, "agd": 5, "ihd": 6, "ajd": 7}}
b = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"IjD": "Aa23", "Gender": "Female", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
a.search_key_value(b, "Gender", "Female")
