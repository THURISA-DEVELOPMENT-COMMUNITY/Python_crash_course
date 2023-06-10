
# Classes

'''
A class is a blueprint or a template that defines the structure 
and behavior of objects. It encapsulates data (attributes) and 
functions (methods) that operate on that data.

'''


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")


# Objects

'''
Objects are instances of a class. They represent specific entities
or instances that have their own unique state and behavior based
on the class definition.

'''

car1 = Car("Toyota", "Camry")
car2 = Car("Ford", "Mustang")

car1.drive()  
car2.drive()  


# Encapsulation

'''
Encapsulation is the practice of hiding internal details and providing
a public interface to interact with an object. It helps in achieving
data abstraction and information hiding.

'''


# Inheritance

'''
Inheritance is a mechanism where a class (derived class or subclass)
inherits properties and behavior from another class (base class or superclass). 
It allows for code reuse and enables the creation of a hierarchical class structure.

'''


class ElectricCar(Car):
    def charge(self):
        print(f"The {self.make} {self.model} is charging.")

electric_car = ElectricCar("Tesla", "Model S")
electric_car.drive()  
electric_car.charge()  
