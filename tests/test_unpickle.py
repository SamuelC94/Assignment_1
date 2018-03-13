from ..database_abstract import DatabaseAbstract
from ..database_local import DBLocal
from ..unpickler import Unpickler
from unittest import TestCase


class TestUnpickler(TestCase):

    def setUp(self):
        self.local = DBLocal()
        self.local.connect()

    def tearDown(self):
        self.local.close()
        self.local = None

    def test_unpickle_dict(self):
        expected = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 2445, "BMI": "normal", "salary": 20,
                        "Birthday": "24/06/1995"},
                    1: {"IhD": "A2f3", "Gender": "Male", "Age": 23, "Sales": 2565, "BMI": "normal", "salary": 20,
                        "Birthday": "24/06/1995"},
                    2: {"IjD": "Aa23", "Gender": "Female", "Age": 25, "Sales": 25, "BMI": "normal", "salary": 20,
                        "Birthday": "24/06/1995"},
                    3: {"IgD": "A23", "Gender": "Female", "Age": 26, "Sales": 225, "BMI": "normal", "salary": 20,
                        "Birthday": "24/06/1995"}}
        data = self.local.insert_dictionary(expected)
        data = data.get_db()
        result = Unpickler.unpickle_dictionary(data)
        # print(result)
        self.assertEqual(expected, result)

    # def test_unpickle_not_pickled(self):
    #     data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
    #                 "Birthday": "24/06/1995"},
    #             1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
    #                 "Birthday": "24/06/1995"},
    #             2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
    #                 "Birthday": "24/06/1995"},
    #             3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
    #                 "Birthday": "24/06/1995"}}
    #     result = self.unpickler.unpickle_dictionary(data)
    #     print(result)
    #     self.assertTrue(True)





