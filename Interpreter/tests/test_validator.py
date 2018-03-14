from ..validator import Validator
from unittest import TestCase


class TestValidator(TestCase):

    def setUp(self):
        self.validator = Validator()

    def tearDown(self):
        self.validator = None

    def test_valid_data(self):
        expected = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "salary": "20 000",
                    "Birthday": "24/06/1992"},
                    2: {"ID": "A233", "Gender": "male", "Age": "27", "Sales": "350", "BMI": "normal", "salary":
                    "20 000", "Birthday": "24/06/1990"},
                    3: {"ID": "A234", "Gender": "Female", "Age": "29", "Sales": "420", "BMI": "normal", "salary":
                    "20 000", "Birthday": "24/06/1988"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "salary": "20 000",
                "Birthday": "24/06/1992"},
                2: {"ID": "A233", "Gender": "male", "Age": "27", "Sales": "350", "BMI": "normal", "salary": "20 000",
                "Birthday": "24/06/1990"},
                3: {"ID": "A234", "Gender": "Female", "Age": "29", "Sales": "420", "BMI": "normal", "salary": "20 000",
                "Birthday": "24/06/1988"}}
        result = Validator.save_dict(data)
        self.assertEqual(expected, result)
