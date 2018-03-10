# From parent folder, file pickler, import class pickler
# INTRA-PACKAGE IMPORT FTW!
from sys import path
path.append("..")
from ..pickler import Pickler
from unittest import TestCase

#
# path = Path(__file__).resolve().parents[1]
# TestLoader(path)


class TestPicklerSetUp(TestCase):
    def setUp(self):
        self.pickler = Pickler()

    def tearDown(self):
        self.pickler.dispose()
        self.pickler = None

    def test_pickle(self):
        key = 1
        value = {"ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}
        print(value)
        result = self.pickler.pickle_record_values(key, value)
        print(result)
        self.assertNotEqual(value, result)






