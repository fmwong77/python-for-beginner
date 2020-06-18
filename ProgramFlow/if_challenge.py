name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

if 18 <= age < 31:
    print("Welcome to the club 18-30 holidays, {}".format(name))
else:
    print("We're sorry that you are not allowed to go on the holiday")