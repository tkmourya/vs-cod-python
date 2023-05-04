class Employee:
    company = "google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")

    def getdetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"the subunit of the employee is {self.subunit}")



    
    # def getsalary(self):
    #     print(f"salary for this employee working in {self.company} is {self.salary}")

    # @staticmethod
    # def greet():                   # without self
    #     print("good morning, sir")

    # @staticmethod
    # def time():                   # without self
    #     print("the time is 9pm in the night")
tarun = Employee("tarun", 100, "you tube")
tarun.getdetails()