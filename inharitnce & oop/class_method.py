class Employee:
    company = "camel"
    salary = 100
    location = "delhi"

    # def changesalary(self, sal):
    #     self.salary = sal

    @classmethod    
    def changesalary(cla, sal):
        cla.salary = sal


e = Employee()
print(e.salary)
e.changesalary(6576)
print(e.salary)
print(Employee.salary)

