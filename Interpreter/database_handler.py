from database_local import DBLocal
from database_remote import DBRemote
from pickler import Pickler
from unpickler import Unpickler


class DatabaseHandler:
    def __init__(self):
        self.local = DBLocal()
        self.remote = DBRemote()
        self.local_connection = None
        self.remote_connection = None

    # A really, really, really bad decorator that can get fixed in ass2 //Wesley
    def local_decorator(f):
        def wrapper(*args):
            db = args[0].local_connection
            args[0].local.connect(db)
            if args[0].local_connection == ":memory:":
                args[0].local.create_table()
            r = f(*args)
            args[0].local.commit()
            args[0].local.close()
            return r
        return wrapper

    def set_local(self, connection):
        self.local_connection = connection

    def set_remote(self, host, user, password, db):
        self.remote_connection = {"host": host, "user": user, "password": password, "db": db}

    @local_decorator
    def insert_local_dict(self, dictionary):
        """Insert values into both the local and remote"""
        pickled = Pickler.pickle_dictionary_values(dictionary)
        self.local.insert_dictionary(pickled)
        print(self.local.get_db())
        # self.remote.insert_dictionary(dictionary)

    @local_decorator
    def create_table(self):
        self.local.create_table()

    @local_decorator
    def get_local(self):
        unpickle = Unpickler.unpickle_dictionary(self.local.get_db())
        print(unpickle)

    # Will do later
    def db_sync(self):
        """Will need to test remote first"""
        pass


    # def local_method(self, function):
    #     """
    #
    #     :param function:
    #     :return:
    #     """
    #     self.local.connect()


# a = DatabaseHandler()
#
# a.set_local("file")
# a.create_table()
# a.insert_local_dict({1: "chachacha", 2: "asd325f15dsa1f51"})
#
# a.get_local()
