class Employee:
    company = "google"
    salary = 100      # class attribute

tarun = Employee()
harsita = Employee()
neha = Employee()
tarun.salary = 200    # instance attribute
neha.salary = 300     # '''''
harsita.salary = 400  # '''''

Employee.company = "you tube" # change company name// changing class attribute
print(tarun.company)
print(harsita.company)
print(neha.company)
print(tarun.salary)
print(harsita.salary)
print(neha.salary)
