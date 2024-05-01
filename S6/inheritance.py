
class vehicle:
    def __init__(self,company,fuel,price):
        self.company = company
        self.fuel = fuel
        self.price = price

    def start_engine(self):
        print("Starting Engine ",self.company)


class car(vehicle):
    def __init__(self,company,fuel,price,color):
        super().__init__(company,fuel,price)
        self.color = color

    def open_roof(self):
        print("opening roof ", self.company)

c = car("BMW","Petrol",21,"Black")

print(c.company)

c.start_engine()
c.open_roof()

v = vehicle("Suzuki","CNG",90)

v.start_engine()

