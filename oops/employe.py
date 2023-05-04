class Employee:
    company = "google"

tarun = Employee()
harsita = Employee()
neha = Employee()


Employee.company = "you tube"
print(tarun.company)
print(harsita.company)
print(neha.company)

