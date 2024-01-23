class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hi(self):
        return f'Hi! My name is {self.name}!'
    
class Student(Person):
    ...


class PoliceOfficer(Person):
    ...


s1 = Student('Ludwig', 30)
print(s1.say_hi())
print()
o1 = PoliceOfficer('Geraldo', 45)
print(o1.say_hi(), "I'm a Police Officer")


