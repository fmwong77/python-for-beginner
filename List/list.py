# ipAddress = input("Please enter an Ip Address")
# print(ipAddress.count("."))
parrot_list = ["non piin", "no more", "a stiff", "bereft of live"]

parrot_list.append("A Norwegien Blue")
for state in parrot_list:
    print("This parrot is {}".format(state))

even = [2,4,6,8,10]
odd = [1,3,5,7,9]

numbers1 = [even + odd] #[[2,4,6,8],[1,3,5,7,9]]

numbers = even + odd
numbers.sort()
print(numbers)
print(numbers.sort()) # return None
numbers_in_order = sorted(numbers)
print(numbers_in_order)

list_1 = []
list_2 = list() #list construtor

if list_1 == list_2:
    print("They're equal")
print(list("The lists are equal"))

even = [2,4,6,8]
another_even = even
another_even.sort(reverse = True)
print(even)

#if you use list(even), they're not the same another more
another_even2 = list(even)
print(another_even2 is even) #refer to the memory address is the 2
print(another_even2 == even) #refer to the value in the list

