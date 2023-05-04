class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"the value of {self.num} square is {self.num**2}")

    def squareroot(self):
        print(f"the value of {self.num} squareroot is {self.num**.5}")

    def cube(self):
        print(f"the value of {self.num} cube is {self.num**3}")

    @staticmethod
    def greet():
        print("****hello there welcome to best calculator of the world!****")


a = calculator(9)
a.greet()
a.square()
a.squareroot()
a.cube()
