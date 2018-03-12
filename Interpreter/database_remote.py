<<<<<<< HEAD
from pymysql import connect as remote_connect
from pymysql import cursors as remote_cursor
from database_abstract import DatabaseAbstract


# Wesley
class DBRemote(DatabaseAbstract):
    # sadly, Wesley, even I don't like this, breaks my soul
    # The default values need to be set so the ABC can still run
    def connect(self, host=None, user=None, password=None, db=None):
        """Use a list to connect to the remote server
            :param host is the host parameter for the remote server
            :param user is the user parameter for the remote server
            :param password is the needed password for the remote server
            :param db selects the database to be used
            This will connect to the remote server and allow access to read/write
            into the database"""
        self.connection = remote_connect(host=host,
                                         user=user,
                                         password=password,
                                         db=db,
                                         charset='utf8mb4',
                                         cursorclass=remote_cursor.DictCursor)

        self.cursor = self.connection.cursor()

    # Wesley
    def insert_record(self, value):
        """Insert a single record into the local database"""
        self.cursor.execute("insert into employee(personal) values(%s)", value)

    # Wesley
    def delete_record(self, key):
        """Delete a single record that matches the key"""
        self.cursor.execute("delete from employee where key = %s", key)

    # Wesley
    def update_record(self, key, value):
        """Rewrite a record that already exists"""
        record = (value, key)
=======
from pymysql import connect as remote_connect
from pymysql import cursors as remote_cursor
from database_abstract import DatabaseAbstract


# Wesley
class DBRemote(DatabaseAbstract):
    # sadly, Wesley, even I don't like this, breaks my soul
    # The default values need to be set so the ABC can still run
    def connect(self, host=None, user=None, password=None, db=None):
        """Use a list to connect to the remote server
            :param host is the host parameter for the remote server
            :param user is the user parameter for the remote server
            :param password is the needed password for the remote server
            :param db selects the database to be used
            This will connect to the remote server and allow access to read/write
            into the database"""

        self.connection = remote_connect(host=host,
                                         user=user,
                                         password=password,
                                         db=db,
                                         charset='utf8mb4',
                                         cursorclass=remote_cursor.DictCursor)

        self.cursor = self.connection.cursor()

    # Wesley
    def insert_record(self, value):
        """Insert a single record into the local database"""
        self.cursor.execute("insert into employee(personal) values(%s)", value)

    # Wesley
    def delete_record(self, key):
        """Delete a single record that matches the key"""
        self.cursor.execute("delete from employee where key = %s", key)

    # Wesley
    def update_record(self, key, value):
        """Rewrite a record that already exists"""
        record = (value, key)
>>>>>>> 6540e0402541687358a943f73273ca0ddaad4381
        self.cursor.execute("update employee set personal = %s where key = %s", record)