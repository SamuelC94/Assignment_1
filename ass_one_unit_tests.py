import unittest
from .validatorz import Validator


a_valid_dict = dict({'empid': "A123", 'gender': "M", 'age': "21",
         'sales': "666", 'bmi': "Normal", 'salary': "111",
         'birthday': "13-12-1994"})

invalid_dict_one = dict({'empid': "a123", 'gender': "q", 'age': "1",
         'sales': "1666", 'bmi': "queer", 'salary': "1111",
         'birthday': "131-12-1994"})

invalid_dict_two = dict({'empid': "a123", 'gender': "q", 'age': "21",
         'sales': "666", 'bmi': "Normal", 'salary': "111",
         'birthday': "13-12-1994"})

vd = Validator()


class TestValidator(unittest.TestCase):
    def test_01_empid(self):
        # check empid is valid
        self.assertTrue(vd.check_empid(a_valid_dict['empid']), True)

    def test_02_gender(self):
        # check gender is valid
        self.assertTrue(vd.check_gender(a_valid_dict['gender']), True)

    def test_03_age(self):
        # check age is valid
        self.assertTrue(vd.check_age(a_valid_dict['age']), True)

    def test_04_sales(self):
        # check sales is valid
        self.assertTrue(vd.check_sales(a_valid_dict['sales']), True)

    def test_05_bmi(self):
        # check bmi is valid
        self.assertTrue(vd.check_bmi(a_valid_dict['bmi']), True)

    def test_06_salary(self):
        # check salary is valid
        self.assertTrue(vd.check_salary(a_valid_dict['salary']), True)

    def test_07_birthday(self):
        # check birthday is valid
        self.assertTrue(vd.check_birthday(a_valid_dict['birthday']), True)

    def test_08_check_all(self):
        self.assertEqual(vd.checker(a_valid_dict), 7)

    def test_08_check_all(self):
        self.assertEqual(vd.checker(invalid_dict_two), 5)

    def test_09_check_invalid_empid(self):
        self.assertEqual(vd.check_empid(invalid_dict_one['empid']), 'False')

    def test_09_check_invalid_gender(self):
        self.assertEqual(vd.check_gender(invalid_dict_one['gender']), False)

    def test_09_check_invalid_age(self):
        self.assertEqual(vd.check_age(invalid_dict_one['age']), False)

    def test_09_check_invalid_sales(self):
        self.assertEqual(vd.check_sales(invalid_dict_one['sales']), False)

    def test_09_check_invalid_bmi(self):
        self.assertEqual(vd.check_bmi(invalid_dict_one['bmi']), False)

    def test_09_check_invalid_salary(self):
        self.assertEqual(vd.check_salary(invalid_dict_one['salary']), False)

#
    # def test_09(self):
    #     self.assertTrue(vd.check_empid(adict['empid']), True)
#
    # def test_10(self):
    #     self.assertTrue(vd.check_empid(adict['empid']), True)


if __name__ == '__main__':
    unittest.main()

