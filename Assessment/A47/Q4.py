class Vehicle:
    def speed(self):
        print("Speed varies for different vehicles")

class car(Vehicle):
    def speed(self):
        print("The car speed is 120 km/h.")

class bike(Vehicle):
    def speed(self):
        print("The bike speed is 80 km/h.")


obj=[car(),bike(),Vehicle()]

for a in obj:
    a.speed()