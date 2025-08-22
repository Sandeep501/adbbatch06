# OOPS

# Inheritance

# type 1 - single Inheritance
class Animal():  # -> parent class / base class
    def sound(self):
        return "animal sound"
    
class Cat(Animal): # ->  child class / derived class
    def sound(self):
        return "Meow's"

class Dog(Animal): # ->  child class / derived class
    def get_dog_detail(self):
        return "This is a German dog"
    
    def sound(self):
        return "Bow bow..."


# cat = Cat()
# print(cat.sound())

# dog = Dog()
# print(dog.sound())

# type 2 - multi level Inheritance

class Animal():  # -> parent class / base class
    def sound(self):
        return "animal sound"
    
    def dummy(self):
        return "dummy method in Animal class"
    
class Cat(Animal): # ->  child class / derived class
    def sound(self):
        return "Meow's"
    
    def get_species_info(self):
        return "this is mammel"

class Dog(Cat): # ->  child class / derived class
    def get_dog_detail(self):
        return "This is a German dog"
    
    def sound(self):
        return "Bow bow..."
    
# dog = Dog()

# print(dog.get_species_info())
# print(dog.dummy())


# type 3 - multiple Inheritance
class Animal():  # -> parent class 1
    def sound(self):
        return "animal sound"
    
    def dummy(self):
        return "dummy method in Animal class"
    
    
class Cat(): # ->  parent class 2
    def sound(self):
        return "Meow's"
    
    def get_species_info(self):
        return "this is mammel"


class Dog(Animal, Cat): # ->  child class / derived class
    def get_dog_detail(self):
        return "This is a German dog"
    
    def sound(self):
        return "Bow bow..."
    
dog = Dog()

print(dog.get_species_info())
print(dog.dummy())

# type 4 - hybrid Inheritance

# assginment