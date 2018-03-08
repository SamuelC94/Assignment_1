from abc import ABCMeta, abstractmethod
from sqlite3 import connect
from pymysql import connect as remote_connect
from pymysql import cursors as remote_cursor


class DatabaseAbstract(metaclass=ABCMeta):

    def __init__(self):
        self.connection = None
        self.cursor = None

    @abstractmethod
    def connect(self, connection):
        pass

    def create_table(self):
        """ Create a table that will be created in the local db
            this will store the key and the persons pickled details"""
        self.cursor.execute("Create table if not exists employee(empkey varchar(5) primary key, personal text)")

    def insert_dictionary(self, dictionary):
        """Write a dictionary with key and pickled values
            into the database"""
        for key, value in dictionary.items():
            self.insert_record(key, value)

    def get_db(self):
        """Return the database as dictionary"""
        self.cursor.execute("select * from employee")
        return self.cursor.fetchall()

    def save(self):
        """Changes to the database need to be committed to the database"""
        self.connection.commit()

    def close(self):
        self.connection.close()

    @abstractmethod
    def insert_record(self, key, value):
        pass

    @abstractmethod
    def delete_record(self, key):
        pass

    @abstractmethod
    def update_record(self, key, value):
        pass


class DBLocal(DatabaseAbstract):

    def connect(self, connection=":memory:"):
        """ create object that connects to the local db
            :memory: can be used for a stored db on the ram
            instead of a file/file location"""
        self.connection = connect(connection)
        self.cursor = self.connection.cursor()

    def insert_record(self, key, value):
        """Insert a single record into the local database"""
        record = (key, value)
        self.cursor.execute("insert into employee values(?, ?)", record)

    def delete_record(self, key):
        """Delete a single record that matches the key"""
        self.cursor.execute("delete from employee where key = ?", key)

    def update_record(self, key, value):
        """Rewrite a record that already exists"""
        record = (value, key)
        self.cursor.execute("update employee set personal = ? where key = ?", record)


class DBRemote(DatabaseAbstract):
    # sadly, Wesley, even I don't like this, breaks my soul
    def connect(self, connection):
        """Use a list to connect to the remote server
            :param connection should contain the key => value
            pairs for:
            - host
            - user
            - password
            - db
            This will connect to the remote server and allow access to read/write
            into the database"""
        self.connection = remote_connect(host=connection['host'],
                                         user=connection['user'],
                                         password=connection['password'],
                                         db=connection['db'],
                                         charset='utf8mb4',
                                         cursorclass=remote_cursor.DictCursor)
        self.cursor = self.connection.cursor()

    def insert_record(self, key, value):
        """Insert a single record into the local database"""
        record = (key, value)
        self.cursor.execute("insert into employee values(%s, %s)", record)

    def delete_record(self, key):
        """Delete a single record that matches the key"""
        self.cursor.execute("delete from employee where key = %s", key)

    def update_record(self, key, value):
        """Rewrite a record that already exists"""
        record = (value, key)
        self.cursor.execute("update employee set personal = %s where key = %s", record)


thing = DBLocal()
thing.connect()
thing.create_table()
thing.insert_record("thing", "omfg, unpickled af!")
print(thing.get_db())

remotething = DBRemote()
# Will need an actual database running with a database called test
aconnect = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'db': 'test',
}

remotething.connect(aconnect)
remotething.create_table()
remotething.insert_record("1w34a", "omfg, unpickled af!")
print(remotething.get_db()[0]['empkey'])

# Classes are currently incomplete
# Still need to be cleaned up, moved around and added functionality
# When using them in a controller type object then do:
# try connect query commit
# except rollback








