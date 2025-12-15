class Vehicle:
    color="white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

school_bus=Bus("volvo",120,12)
print("--------------vehical 1-------------\n")
print("color:",school_bus.color,"\nname:",school_bus.name,"\nspeed:",school_bus.max_speed,"\nmileage",school_bus.mileage)

car1=Car("audi",220,10)
print("--------------vehical 2-------------\n")
print("color:",car1.color,"\nname:",car1.name,"\nspeed:",car1.max_speed,"\nmileage",car1.mileage)
