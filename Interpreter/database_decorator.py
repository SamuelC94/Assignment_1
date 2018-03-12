from abc import ABCMeta, abstractmethod


class DatabaseDecorateAbstract(metaclass=ABCMeta):
    def __init__(self):
        self.connection = None
        self.details = None

    @abstractmethod
    def __call__(self, f):
        pass


class DBDecorateLocal(DatabaseDecorateAbstract):
    def __call__(self, f):
        def wrapped(*args):
            details = args[0].local_connection
            args[0].local.connect(details)


# Wesley, this hurt my brain
class DatabaseDecorator:
    def __init__(self):
        self.connection = None
        self.details = None

    def __call__(self):
        # self.connection.close()
        # self.connection.connect(details["host"], details["user"], details["password"], details["db"])
        # self.connection.commit()

        def wrapper():
            print("Inside")

            def wrapped(*args):
                print("testerything")
                args[0].local_connection = "hehehe"
                print(args[0])
                return f(*args)
            return wrapped()

        print("please be last")
        return wrapper()

