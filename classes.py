# python classes

class Car:
    brand = "Toyota"
    color = "Black"
    
    def drive(self):
        return f"{self.brand} Car is running"


# car1 = Car() # class object instance
# print(car1.brand)
# print(car1.drive())


# car2 = Car()
# print(car2.brand)
# print(car2.drive())

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        return f"{self.brand} Car is running"
    

# car1 = Car(brand="Kia", color="Brown")
# print(car1.drive())

# car2 = Car(brand="Honda", color="white")
# print(car2.drive())

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    
    def study(self):
        return f"{self.name} is studying.."
    
    
    def show_details(self, medium="Engish", rank=-1):
        return f"{self.name}, {self.age}, {self.grade}, {medium}"

s1 = Student("Gowtham", 5, 1)
s2 = Student("Likith", 7, 2)

print(s1.study())
print(s2.show_details())
print(s2.show_details("Telugu"))