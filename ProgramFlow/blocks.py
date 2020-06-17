# for i in range(1, 13):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
# print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))
print(age)

if age < 18:
    print("Pleas come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You're old enough to vote")
    print("Please put an X in the box")