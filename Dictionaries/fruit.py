fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit)

vege = {"cabbage": "every child's favourite",
        "sprout": "mmmm, lovely",
        "spinach": "can I have some more fruits, please"}
# print(vege)
# vege.update(fruit)
# print(vege)
nice_and_nasty = fruit.copy()
nice_and_nasty.update(vege)
print(nice_and_nasty)
print(fruit)
print(vege)