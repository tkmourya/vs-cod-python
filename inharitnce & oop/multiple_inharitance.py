class employee:
    company = "visa"
    ecode = 122

class freelancer:
    company = "fiverr"
    level = 0

    def upgradlevel(self):
        self.level = self.level + 1

class programmer(employee, freelancer):
    name ="rohit"

p = programmer()
p.upgradlevel()
print(p.level)
print(p.company)
print(p.ecode)

