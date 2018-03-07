from pathlib import Path
import csv


class FileHandler:
    def __init__(self, file_name):
        self.filename = file_name

    @staticmethod
    def load_file():
        cwd = './Saves/'
        for file in Path(cwd).iterdir():
            print(file)
        file = input("Which file do you wish to load? >>> ")
        filename = Path(cwd+file)
        return filename

    def file_exist(self):
        if self.filename.exists():
            return True
        else:
            return False

    def csv_read(self):
        with open(self.filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)


def run():
    a = FileHandler.load_file()
    aclass = FileHandler(a)

    while aclass.file_exist() is False:
        print("File exists:", aclass.file_exist())
        a = FileHandler.load_file()
        aclass = FileHandler(a)
    if aclass.file_exist() is True:
        aclass.csv_read()
