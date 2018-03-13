import re


class Validator:
    def __init__(self):
        self.valid_dict = dict()
        self.empno = ""
        self.empid = "^[A-Z][\d]{3}$"
        self.gender = "^(M|F)$"
        self.age = "^[\d]{2}$"
        self.sales = "^[\d]{3}$"
        self.BMI = "^(Normal|Overweight|Obesity|Underweight)$"
        self.salary = "^[0-9]{2,3}$"
        # James (new reg ex)
        self.birthday = "^(0[1-9]|[1-2][0-9]|3(0|1))(-|/)(0[1-9]|1[0-2])(-|/)(19|20)[0-9]{2}$"

    def check_empid(self, new_empid):
        # self.current_empno = empno
        match = re.match(self.empid, new_empid)
        if match:
            new_empid = True
            return new_empid
        else:
            new_empid = False
            return new_empid

    def check_gender(self, new_gender):
        # self.current_empno = empno
        match = re.match(self.gender, new_gender)
        if match:
            new_gender = True
            return new_gender
        else:
            # James (new reg ex)
            match = re.match("^((m|M)ale)$", new_gender)
            if match:
                new_gender = "M"
                return new_gender
            match = re.match("^((f|F)emale)$", new_gender)
            if match:
                new_gender = "F"
                return new_gender
            new_gender = False
            return new_gender

    def check_age(self, new_age):
        # self.current_empno = empno
        match = re.match(self.age, new_age)
        if match:
            new_age = True
            return new_age
        else:
            new_age = "False"
            return new_age

    def check_sales(self, new_sales):
        # self.current_empno = empno
        match = re.match(self.sales, new_sales)
        if match:
            new_sales = True
            return new_sales
        else:
            new_sales = False
            return new_sales

    def check_bmi(self, new_BMI):
        # self.current_empno = empno
        match = re.match(self.BMI, new_BMI)
        if match:
            new_BMI = True
            return new_BMI
        else:
            # James (new reg ex)
            match = re.match("^(normal|overweight|obesity|underweight)$", new_BMI)
            if match:
                new_BMI = new_BMI.capitalize()
                return new_BMI
            new_BMI = False
            return new_BMI

    def check_salary(self, new_salary):
        # self.current_empno = empno
        match = re.match(self.salary, new_salary)
        if match:
            new_salary = True
            return new_salary
        else:
            new_salary = False
            return new_salary

    def check_birthday(self, new_birthday):
        # self.current_empno = empno
        match = re.match(self.birthday, new_birthday)
        if match:
            new_birthday = True
            return new_birthday
        else:
            # James (new reg ex)
            invalid_delims = "^(/|\\|.|:|;|,|_)$"
            match = re.match(invalid_delims, new_birthday)
            if match:
                new_birthday.replace(invalid_delims, '-')
            new_birthday = False
            return new_birthday

    # James
    def checker(self, loaded_dict):
        result = 0
        for item in loaded_dict.items():
            if item[0] == "empid":
                if a.check_empid(item[1]) is True:
                    result += 1
                else:
                    return "empid error" + " = " + item[1]
            elif item[0] == "gender":
                if a.check_gender(item[1]) is True:
                    result += 1
                else:
                    return "gender error" + " = " + item[1]
            elif item[0] == "age":
                if a.check_age(item[1]) is True:
                    result += 1
                else:
                    return "age error" + " = " + item[1]
            elif item[0] == "sales":
                if a.check_sales(item[1]) is True:
                    result += 1
                else:
                    return "sales error" + " = " + item[1]
            elif item[0] == "bmi":
                if a.check_bmi(item[1]) is True:
                    result += 1
                else:
                    return "bmi error" + " = " + item[1]
            elif item[0] == "salary":
                if a.check_salary(item[1]) is True:
                    result += 1
                else:
                    return "salary error" + " = " + item[1]
            elif item[0] == "birthday":
                if a.check_birthday(item[1]) is True:
                    result += 1
                else:
                    return "birthday error" + " = " + item[1]
        return result

    def save_dict(self, loaded_dict):
        b = a.checker(loaded_dict)
        # Error, need another loop "while checker() is running"
        if b is False:
            print("Error at entry: " + str(self.current_empno))
        else:
            record = dict()
            record[b] = loaded_dict[self.current_empno].get(b)
            self.valid_dict[self.current_empno] = record
        print(self.valid_dict)


a = Validator()

# 1	January	        31 days
# 2	February        28 days, 29 in leap years
# 3	March           31 days
# 4	April           30 days
# 5	May	            31 days
# 6	June	        30 days
# 7	July	        31 days
# 8	August	        31 days
# 9	September	    30 days
# 10 October	    31 days
# 11 November	    30 days
# 12 December	    31 days



def checker_two(loaded_dict):
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
                a.check_bmi(item[1])
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
