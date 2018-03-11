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
    def pickle_dictionary_values(self, clear_dict):
        """Create a dictionary with pickled values, the key will remain the same"""
        for key, value in clear_dict:
            self.pickle_dict[key] = dumps(value)
        # return self.pickle_dict

    # Sam
    def get_pickled_dictionary(self):
        return self.pickle_dict

    # Sam
    @staticmethod  # does this need to be static??
    def pickle_dict(dictionary):  # (self, dictionary) (if not static)
        pickled_dict = dumps(dictionary)  # pickled_super_dict's data type is now a byte stream
        return pickled_dict  # returns a byte stream to be saved in database


# check that it creates byte stream

# tester = Pickler()
# print(type(tester))
# b = tester.pickle_super_dict({"ONE", "THE NUMBER ONE"})
# print(type(b))


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



