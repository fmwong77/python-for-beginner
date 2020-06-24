string = "1234567890"
my_iterator = iter(string)

for i in range(0,len(string)):
    print(next(my_iterator))

for i in string:
    print(i)