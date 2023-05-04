class Employee:
    company = "google"
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")

tarun = Employee()
tarun.salary = 100000
tarun.getsalary() # Employee.getsalary()


