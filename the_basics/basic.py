import datetime
print(datetime.datetime.now())

x = 10
y = "string"
print(type(y))

student_grades = [9.1, 8.8, 7.5]
result = student_grades.count(9.1)
print(result)
# result = sum(student_grades) / len(student_grades)
# print(max(student_grades))

# list is mutable
list1 = [1, 2, 3, 4]
list1.append(5)
print(list1)
list1.__delitem__(0)
print(list1)

# tuple is immutable
tuple1 = (1, 2, 3, 4)
# tuple1.append(5)
print(tuple1)


