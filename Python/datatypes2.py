# datatypes

# 1. Lists --> memory allocation would be dynamic, lists are mutable

marks = [80, 40, 56, 67, 39]

# add new value
# marks.append(100)

# remove the last element in the list
# marks.pop()

# modify the values in the List
# marks[3] = 77

# marks.remove(56)

# marks.insert(5, 45)

# print(marks.index(45))

# marks2 = [44, 33, 22]

# marks.extend(marks2)
# print(marks)

# print(marks + marks2)




# Tuples

nums = (1, 2, 3, 4)

# nums.append(5)
# print(nums)

# print(nums)


# sets

nums = {'a', 10, 12, 12, 1, 100, 400, 'd', 'c', 'k', 2, 3, 3, 3, 4, 5, 6, 6}
# print(nums)


# dict

student = {
    "Name": "Sandeep",
    "Age": 29,
    "Subject": "ADB"
}

print(student["Name"])

print(student["Age"])

student["Age"] = 28

student["Exp"] = 6

print(student.keys())
print(student.values())



print(student)