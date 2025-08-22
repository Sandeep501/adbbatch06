# functions or methods

# def add_numbers(para1, para2):
#     return para1 + para2


# dy Snamic with parameters
def add_numbers(para1: int, para2: int) -> int:
    return para1 + para2

# function call is mandatory
# print(add_numbers(100, 300))
# print(add_numbers("10", 458))
# print(add_numbers(10, 359))

# static function
def greet():
    return "Good Evening!"

# print(greet())


# name = input("Please enter your name: ")

#Sandeep --> 3 vowels
# vowels = a, e, i, o, u


# write a function to count the no.of vowels present in a string

def count_vowels(name: str) -> int:
    if isinstance(name, str):
        vowels = ('a', 'e', 'i', 'o', 'u')
        cnt = 0
        for char in name.lower():
            if char in vowels:
                cnt = cnt + 1
            
        return cnt
    else:
        return "Please enter only string values!"

# print(count_vowels(name))

# numbers = []

# numbers.append(1)
# numbers.append(2)
# .
# .
# .
# numbers.append(10)

# for i in range(1, 11):
#     if i%2 == 0:
#         numbers.append(i)
    
# print(numbers)
# list comprehension

numbers = [i for i in range(1, 11) if i%2 == 0]
print(numbers)