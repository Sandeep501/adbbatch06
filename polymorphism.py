# poly-morphism
# live or live

class Dog():
    def sound(self):
        return "Barks"
    
class Cat:
    def sound(self):
        return "Meow"
    
class Cow():
    def sound(self):
        return "Amba"

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    print(animal.sound())
