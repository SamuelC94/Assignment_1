import re


class Validator:
    def __init__(self):
        self.empid = "^[A-Z][\d]{3}$"
        self.gender = "M|F"
        self.age = "^[\d]{2}$"
        self.sales = "^[\d]{3}$"
        self.BMI = "^(Normal|Overweight|Obesity|Underweight)$"
        self.salary = "^[\d]{2,3}$"
        self.birthday = "^[1-31](-|/)[1-12](-|/)(19|20)[0-9]{2}$"

    def check_empid(self, new_empid):
        match = re.match(self.empid, new_empid)
        if match:
            return new_empid
        else:
            new_empid = "Invalid empid"
            return new_empid

    def check_gender(self, new_gender):
        match = re.match(self.gender, new_gender)
        if match:
            return new_gender
        else:
            new_gender = "Invalid gender"
            return new_gender

    def check_age(self, new_age):
        match = re.match(self.age, new_age)
        if match:
            return new_age
        else:
            new_age = "Invalid age"
            return new_age

    def check_sales(self, new_sales):
        match = re.match(self.BMI, new_sales)
        if match:
            return new_sales
        else:
            new_sales = "Invalid sales"
            return new_sales

    def check_BMI(self, new_BMI):
        match = re.match(self.BMI, new_BMI)
        if match:
            return new_BMI
        else:
            new_BMI = "Invalid BMI"
            return new_BMI

    def check_salary(self, new_salary):
        match = re.match(self.BMI, new_salary)
        if match:
            return new_salary
        else:
            new_salary = "Invalid salary"
            return new_salary

    def check_birthday(self, new_birthday):
        match = re.match(self.birthday, new_birthday)
        if match:
            return new_birthday
        else:
            new_birthday = "Invalid birthday"
            return new_birthday


a = Validator()


def checker(loaded_dict):
    for empno, row in loaded_dict.items():
        for item in row.items():
            if item[0] == "ID":
                a.check_empid(item[1])
            elif item[0] == "Gender":
                a.check_gender(item[1])
            elif item[0] == "Age":
                a.check_age(item[1])
            elif item[0] == "Sales":
                a.check_sales(item[1])
            elif item[0] == "BMI":
                a.check_BMI(item[1])
            elif item[0] == "Salary":
                a.check_salary(item[1])
            elif item[0] == "Birthday":
                a.check_birthday(item[1])


#z1 = "A12"
#z2 = "M"
#z3 = "21"
#z4 = "Normal"
#z5 = "100"
#z6 = "13-12-1994"
#
#
#c = a.check_empid(z1)
#d = a.check_empid(z2)
#e = a.check_empid(z3)
#f = a.check_empid(z4)
#g = a.check_empid(z5)
#h = a.check_empid(z6)
#print(z1)
#print(z2)
#print(z3)
#print(z4)
#print(z5)
#print(z6)
