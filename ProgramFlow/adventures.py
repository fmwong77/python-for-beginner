available_exits = ["north", "south", "east", "west"]

chosen_exits = ""
while chosen_exits not in available_exits:
    chosen_exits = input("Please choose a direction: ")
    if chosen_exits.casefold() == 'quit':
        print("Game over")
        break
else:
    print("aren't you glad you got out of here")

# for i in range(0, 100, 7):
#     if i > 0 and i % 11 == 0:
#         break
#     print(i)