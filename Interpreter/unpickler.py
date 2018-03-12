from pickle import Unpickler as Unpick
from io import BytesIO


# Wesley
class Unpickler:

    # Wesley
    def __init__(self):
        self.unpickled_dict = {}

    # Wesley
    def unpickle_dictionary(self, dictionary):
        """Input a dictionary with key value
            where value is pickled and return a dictionary
            with unpickled values"""
        # need the items function to iterate through dictionary
        for key, value in dictionary.items():
            # Create object that will be treated as a file for unpickling
            file = BytesIO(value)
            self.unpickled_dict[key] = Unpick(file).load()
        return self.unpickled_dict

#       Create function to unpickle a key => value pair instead of entire dictionary?
#       Create function to return the stored dictionary?


