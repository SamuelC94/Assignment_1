from database_local import DBLocal
from database_remote import DBRemote
# from database_decorator import DatabaseDecorator
from pickler import Pickler
from unpickler import Unpickler


class DatabaseHandler:
    def __init__(self):
        self.local = DBLocal()
        self.remote = DBRemote()
        self.local_connection = None
        self.remote_connection = None

    # A really, really, really bad decorator, ummmm James did ? //Wesley
    def local_decorator(f):
        def wrapper(*args):
            # print("before")
            # print("Starting" + f.__name__)
            db = args[0].local_connection
            args[0].local.connect(db)
            if args[0].local_connection == ":memory:":
                args[0].local.create_table()
            #     If it is stored memory then it will all be destroyed
            r = f(*args)
            args[0].local.commit()
            args[0].local.close()
            # print("Finished")
            # print("After decorated function")
            return r
        return wrapper

    def set_local(self, connection):
        self.local_connection = connection

    def set_remote(self, host, user, password, db):
        self.remote_connection = {"host": host, "user": user, "password": password, "db": db}

    def test(self, eh, ah):
        print("Used a function")
        # print(eh)
        # print("thing" + self.local_connection)

    def check(self):
        print(self.local_connection)

    @local_decorator
    def insert_local_dict(self, dictionary):
        """Insert values into both the local and remote"""
        self.local.insert_dictionary(dictionary)
        print(self.local.get_db())
        # self.remote.insert_dictionary(dictionary)

    @local_decorator
    def create_table(self):
        self.local.create_table()

    def db_sync(self):
        """Will need to test remote first"""
        pass

    def local_update(self, dictionary):
        """Update the local database with file"""
        pickle = Pickler.pickle_dictionary_values(dictionary)
        self.local.connect()


    # def local_method(self, function):
    #     """
    #
    #     :param function:
    #     :return:
    #     """
    #     self.local.connect()


a = DatabaseHandler()

a.set_local(":memory:")
a.create_table()
a.insert_local_dict({1: "chachacha", 2: "asd325f15dsa1f51"})

