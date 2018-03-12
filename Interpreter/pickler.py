from pickle import dumps
# from unpickler import Unpickler
# from DB_Local import DBLocal
# from collections import namedtuple


# Wesley
class Pickler:

    # # Wesley - not needed anymore
    # def __init__(self):
    #     self.pickle_dict = {}
    #
    # # Wesley
    # def pickle_record_values(self, key, value):
    #     """ Pickle a record and add to a dictionary
    #         :param1 key, will be the key defined in the dictionary
    #         :param2 value, will be pickled
    #         No return provided
    #         """
    #     self.pickle_dict[key] = dumps(value)
    #     return self.pickle_dict

    # Wesley
    @staticmethod
    def pickle_dictionary_values(dictionary):
        """Create a dictionary with pickled values, the key will remain the same"""
        pickled_dict = dict()
        for key, value in dictionary.items():
            pickled_dict[key] = dumps(value)
        return pickled_dict



