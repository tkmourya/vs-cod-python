class Employee:
    company = "google"
    
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():                   # without self
        print("good morning, sir")

    @staticmethod
    def time():                   # without self
        print("the time is 9pm in the night")



tarun = Employee()
tarun.salary = 100000
tarun.getsalary() # Employee.getsalary()
tarun.greet()  # Employee.greet()
tarun.time()
