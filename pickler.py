from pickle import dumps
# from unpickler import Unpickler
# from DB_Local import DBLocal
# from collections import namedtuple


# Wesley
class Pickler:

    # Wesley
    def __init__(self):
        self.pickle_dict = {}

    # Wesley
    def pickle_record_values(self, key, value):
        """ Pickle a record and add to a dictionary
            :param1 key, will be the key defined in the dictionary
            :param2 value, will be pickled
            No return provided
            """
        self.pickle_dict[key] = dumps(value)
        return self.pickle_dict

    # Wesley
    def pickle_dictionary_values(self, dictionary):
        """Create a dictionary with pickled values, the key will remain the same"""
        for key, value in dictionary:
            self.pickle_dict[key] = dumps(value)
        return self.pickle_dict

    # using a function to get the dictionary instead of returning each time it changes
    # def get_dictionary(self):

# Just shows that everything works
# thing = Pickler()
# thing.pickle_record_values("hey", "aslkdjflasdkj3r325")
# thing.pickle_record_values("he1y", "aslkdjflasdkj34r325")
# thing.pickle_record_values("h3ey", "aslkdjflasd4kj3r325")
# pickled_dict = thing.pickle_record_values("he2y", "aslkdjflasdkj123r325")
# #
# # print(pickled_dict)
# # #
# aThing = Unpickler()
#
# unpickled_dict = aThing.unpickle_dictionary(pickled_dict)
# # print(unpickled_dict)
#
# conn = DBLocal()
#
# conn.connect(":memory:")
# conn.create_table()
# conn.insert_dictionary(pickled_dict)
# print(dict(conn.get_db()))



