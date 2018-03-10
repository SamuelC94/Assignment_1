from pathlib import Path
import csv
import os
from validator import checker


class FileHandler:
    def __init__(self, file_name):
        self.filename = file_name

    @staticmethod
    def load_file():
        cwd = './Saves/'
        print(os.listdir(cwd))
        file = input("Which file do you wish to load? >>> ")
        filename = Path(cwd+file)
        return filename

    def file_exist(self):
        if self.filename.exists():
            return True
        else:
            return False

    def csv_read(self):
        data = dict()
        empno = 0
        with open(self.filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                record = dict()
                for key in row:
                    record[key] = row.get(key)
                data[empno] = record
                empno += 1
            print(data)
        return data


def run():
    a = FileHandler.load_file()
    aclass = FileHandler(a)

    while aclass.file_exist() is False:
        print("File exists:", aclass.file_exist())
        a = FileHandler.load_file()
        aclass = FileHandler(a)
    if aclass.file_exist() is True:
        #aclass.csv_read()
        checker(aclass.csv_read())
