class Employee:
    company = "google"

    def showdetails(self):
        print("this is an employee")

class programmer(Employee):
    language = "python"
    company = "youtube"

    def getlanguage(self):
        print(f"the language is {self.language}")

    def showdetails(self):
        print("this is an programmer")

e = Employee()
e.showdetails()
p = programmer()
p.showdetails()
print(p.company)

    