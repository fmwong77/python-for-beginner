my_list = list(range(10))
print(my_list)

even = list(range(0,10,2))
odd = list(range(1,10,2))
print(even)
print(odd)

string = "abcdefghijklmn"
print(string.index("e"))
print(string[4])

small_decimal = range(0,10)
my_range = small_decimal[::2]
print(my_range.index(4))

print(range(0,100)[::-2] == range(99,0,-2))

print("#" * 10)
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
    print(i)
