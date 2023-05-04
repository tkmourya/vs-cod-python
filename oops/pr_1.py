
class programmer:
    company = "microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getinfo(self):
        print(f"the name of the {self.company} programmer is {self.name} and the product is {self.product}")

tarun = programmer("tarun", "skype")
alka = programmer("alka", "gitHub")
tarun.getinfo()
alka.getinfo()