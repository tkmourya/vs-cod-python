"[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
class train:
    def __init__(self, name, fare, seats) -> None:
        self.name = name
        self.fare = fare 
        self.seats = seats
    def getstatus(self):
        print("---------------------------------------------------")
        print(f"the name of the train is {self.name}")
        print(f"the seats available in the train is {self.seats}")
        print("---------------------------------------------------")
    def fareinfo(self):
        print(f"the price of the ticket is: rs. {self.fare}")

    def bookticket(self):
        if(self.seats>0):
            print(f"your ticket has been booked! your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("sorry this train is full! kindely try in tatkal")

    def cancelticket(self, seatNo): # timeslap 9:44
        pass
intercity = train("intercity express: 14140", 90, 10)
intercity.getstatus()
intercity.bookticket()
intercity.bookticket()
intercity.getstatus()

