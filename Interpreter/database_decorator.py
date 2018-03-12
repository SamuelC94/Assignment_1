from database_local import DBLocal


class DatabaseDecorator:
    def __init__(self, function, database):
        function()

    def __call__(self):
        print("hey")

