# student_grades = {"Mary":98, "Brian":100, "Cheryl":100}
# for item in student_grades.items():
#   print(item)

# for key in student_grades.keys():
#   print(key)

# for value in student_grades.values():
#   print(value)

# for name, grade in student_grades.items():
#   print("{} has {}".format(name, grade))
#   print("%s has %s" % (name, grade))

# # divide the items in a list by 10 (list comprehension)
# lists = [10,20,30,40,50,-60] 
# result = [list / 10 for list in lists if list > 0]
# print(result)

# result = [list / 10 if list > 0 else 0 for list in lists]
# print(result)

# def foo(lists):
#     # sum = 0
#     # for list in lists:
#     #     sum = sum + float(list)

#     # return sum
#   result_list = [float(list) for list in lists]
#   return sum(result_list)

# print(foo(['1.2', '2.6', '3.3']))

# def foo(lists):
#   result_list = [float(list) for list in lists]
#   return sum(result_list)

# keyword arguments
def foo1(a, b):
  return a + b
  
print(foo1(a=1, b=2))
# non keyword argument
foo1(1, 2)

# keyword arbitrary arguments
def foo_kwargs(**kwargs):
  return kwargs

foo_kwargs(b=1,a=2)
