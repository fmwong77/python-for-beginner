fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit["apple"])
# fruit["pear"] = "an odd shape apple"
# print(fruit["pear"])
# del fruit["pear"]
# fruit.clear()

# while True:
#     dict_key = input("Please enter a key: ")
#     if dict_key.casefold() == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)
    # if dict_key in fruit:
    #     print(fruit.get(dict_key))
    # else:
    #     print(None)

# ordered_key = list(fruit.keys())
# ordered_key.sort()
ordered_key = sorted(list(fruit.keys()))
for f in ordered_key:
    print(f + " - " + fruit[f])

print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + "is " + description)

print(dict(f_tuple))
