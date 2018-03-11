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

    def txt_reader(self):
        empno = 0
        try:
            file = open('testdata.txt', 'r')
            for line in file:
                dictionary = dict()
                rows = line.spit(":")

                for row in rows:
                    if len(row.split("=")) == 2:
                        key = row.split("=")[0]
                        value = row.split("=")[1]
                        value = value.rstrip('\n')
                        dictionary[key] = value
                    else:
                        print("File error")
                        return False
            return dictionary
        finally: print("something weird happened... guys pls send help")





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

