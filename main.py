import datetime

class Student:
    def __init__(self,name, surname, birthdate, height=160):
        if type(name) != str:
            raise TypeError(f"Name must be str. Not a '{type(name).__name__}'")
        if type(surname) != str:
            raise TypeError(f"Surname must be str. Not a '{type(surname).__name__}'")
        if type(birthdate) != str:
            raise TypeError(f"Birthdate must be str, not '{type(birthdate).__name__}'")
        self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
        if self.birthdate > datetime.datetime.now():
            raise ValueError(f"Birthdate cannot be in the future: {self.birthdate.strftime('%d.%m.%Y')}")
        if not isinstance(height, (int, float)):
            raise TypeError(f"Height must be int or float, not '{type(height).__name__}'")
        if height <= 0:
            raise ValueError(f"Height must be greater than zero, not '{height}'")

        self.name = name
        self.surname = surname
        # 25.10.2006
        self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
        self.height = height
        print(f"I am {self.name}")

    def printStudent(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Birthdate: {self.birthdate.strftime('%d.%m.%Y')}")
        print(f"Height: {self.height}")

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nBirthdate: {self.birthdate.strftime('%d.%m.%Y')}\nHeight: {self.height}\n"

    def __int__(self):
        age = (datetime.datetime.now()-self.birthdate)
        return int(age.days / 365)




# створення об'єкта
first_student = Student('vlad', 'karlinskij', '25.10.2006',186)
second_student = Student('oleg', 'palkin', '25.5.2000',220)

first_student.printStudent()

print('------------------------------')
print(type(first_student.__str__()))
print(first_student)
print('------------------------------')
print(type(first_student.__int__()))
print(int(first_student))

