from database_local import DBLocal
from database_remote import DBRemote
from pickler import Pickler
from unpickler import Unpickler


class DatabaseHandler:

    def __init__(self):
        self.local = DBLocal()
        self.remote = DBRemote()

    def db_new_insert_dict(self, dictionary):
        """Insert values into both the local and remote"""
        self.local.insert_dictionary(dictionary)
        self.remote.insert_dictionary(dictionary)

    def db_sync(self):
        """Will need to test remote first"""
        pass
