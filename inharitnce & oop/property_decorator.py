class Employee:
    company = "bharat gas"
    salary = 5600
    salarybonus =  400
    # totalsalary = 6100


    @property
    def totalsalary(self):
        return self.salary + self.salarybonus


    @totalsalary.setter
    def totalsalary(self, val):
        self.salarybonus = val-self.salary

e = Employee()
print(e.totalsalary)
e.tatalsalary = 5800
print(e.salary)
print(e.salarybonus)