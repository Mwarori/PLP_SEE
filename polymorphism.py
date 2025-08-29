# Base class (optional, for structure)
class Vehicle:
    def move(self):
        pass  # This will be overridden in subclasses

# Subclasses
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Bike(Vehicle):
    def move(self):
        print("Riding 🚴")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Demonstration
vehicles = [Car(), Plane(), Bike(), Boat()]

for v in vehicles:
    v.move()
