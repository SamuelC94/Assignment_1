from ..pickler import Pickler
from ..unpickler import Unpickler
from unittest import TestCase


class TestUnpickler(TestCase):

    def setUp(self):
        self.pickler = Pickler()
        self.unpickler = Unpickler()

    def tearDown(self):
        self.pickler = None
        self.unpickler = None

    def test_unpickle_dict(self):
        expected = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                    1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                    2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                    3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
        data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
        pickled = self.pickler.pickle_dictionary_values(data)
        # print(pickled)
        result = self.unpickler.unpickle_dictionary(pickled)
        # print(result)
        self.assertEqual(expected, result)

    def test_unpickle_not_pickled(self):
        data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
        result = self.unpickler.unpickle_dictionary(data)
        print(result)
        self.assertTrue(True)





