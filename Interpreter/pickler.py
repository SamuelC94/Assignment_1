from pickle import dumps
# from unpickler import Unpickler
# from DB_Local import DBLocal
# from collections import namedtuple


# Wesley
class Pickler:
    # Wesley
    @staticmethod
    def pickle_dictionary_values(dictionary):
        """Create a dictionary with pickled values, the key will remain the same"""
        pickled_dict = dict()
        for key, value in dictionary.items():
            pickled_dict[key] = dumps(value)
        return pickled_dict



