# conditional operators

# num = int(input("Enter a Number: "))
# print(type(num))

# if num > 50:
#     print(num, "is greater then -", 50)
# elif num > 10:
#     print(num, "is greater then -", 10)
# else:
#     print(num, "is less then -", 10, "and also", 50)
    
# ---------------------------------------------------

# match

num = int(input("Enter a Number: "))

match (num%2, num > 0):
    case (0, True):
        print("Even and Positive")
    case (0, False):
        print("Even and Negative")
    case (1, True):
        print("Odd and Positive")
    case (1, False):
        print("Odd and Negative")

    