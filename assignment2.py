
"""
This classes demonstrates polymorphism by overriding
the move method from the Vehicle parent class
"""

class Vehicle:
    def move(self):
        # Base move method, meant to be overridden in subclasses
        raise NotImplementedError("Subclass must implement the move method.")

class Car(Vehicle):
    def move(self):
        # Car's version of move
        print("The car is driving on the road.")

class Plane(Vehicle):
    def move(self):
        # Plane's version of move
        print("The plane is flying in the sky.")

class Drone(Vehicle):
    def move(self):
        # Drone's version of move
        print("The drone is flying in the air with high precision.")

# Create objects of Car, Plane, and Drone
car = Car()
plane = Plane()
drone = Drone()

# Call move() on each vehicle object
car.move()
plane.move()
drone.move()
