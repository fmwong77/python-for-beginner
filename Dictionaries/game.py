locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
vocabulary = {"QUIT": "Q",
              "SOUTH": "S",
              "NORTH": "N",
              "WEST": "W",
              "EAST": "E"}
namedExits = {1: {"2": 2, "3": 3, "4": 4, "5": 5},
              2: {"5": 5},
              3: {"1": 1},
              4: {"1": 1, "2": 2},
              5: {"2": 2, "1": 1}}
loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # print(availableExits)
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()

    if len(direction) > 1:
        # for word in vocabulary:
        #     if word in direction:
        #         direction = vocabulary[word]
        words = direction.split()
        for word in words:
            print(word)

            if word in vocabulary.keys():
                direction = vocabulary[word]
                break

    print()
    print(direction)
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")

# print(''.join(locations[0]))