# use else with loop
numbers = [1,45,32,12,60]

for number in numbers:
    if number % 8 == 0:
        print("The numbers are unacceptable")
else:
    print("All those numbers are fine")