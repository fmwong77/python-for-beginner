#         -14
# parrot = "Norwegian Blue"
#
# print(parrot)
#
# # print(parrot[3])
#
# string = "we win"
#
# for i in range(0,6):
#     print(string[i])
# print()
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
# print()
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
# print()
# print(parrot[3-14]) # result is the same as above, negative index starts at -1 backward
# print(parrot[4-14])
# print(parrot[9-14])
# print(parrot[3-14])
# print(parrot[6-14])
# print(parrot[8-14])
#
# # slice
# print(parrot[0:6]) # Norweg, up to but not including index 6
# print(parrot[3:5]) # we
# print(parrot[:9]) #  Norwegian
# print(parrot[10:14]) # Blue
# print(parrot[10:]) # Blue
# print(parrot[:6] + parrot[6:])
# print(parrot[:])
# print(parrot[-4:-2]) # Bl

# step
# print(parrot[0:6:2])
number = "9,223;372:036 854,775;807"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
