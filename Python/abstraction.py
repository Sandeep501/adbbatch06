# abstraction

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        return "Car has started..."
    
    def stop(self):
        return "Car has stopped...."


class Bike(Vehicle):
    def start(self):
        return "Bike has started..."


car1 = Car()
print(car1.start())
print(car1.stop())


bike1 = Bike()
print(bike1.start())