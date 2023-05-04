class Person:
    country = "India"

    def __init__(self):
        print("initializing person...\n")


    def takebreath(self):
        print("i am breathing...")

class Employee(Person):
    company = "honda"

    def getsalary(self):
        print(f"salary is {self.salary}")
        
    def takebreath(self):

        print("i am an employee so i am luckily breathing...")

class Programmer(Employee):
    company ="fiverr"

    def getsalary(self):
        print("no salary to programmer")

    def takebreath(self):
        super().takebreath()
        print("i am an programmer so i am luckily breathing++.")
p = Person()
p.takebreath()
e = Employee()
print(e.company)
e.takebreath()
pr = Programmer()

pr.takebreath()