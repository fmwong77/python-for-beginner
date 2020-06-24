message = """
Please choose your option from the list below:
1. Learn Python
2. Learn Java
3. Go swimming
4. Have dinner
5. Go to bed
0. Exit
"""
choice = "-"
while choice != "0":
    if choice in "12345":
        print("You've chosen {}".format((choice)))
    else:
        print(message)
    choice = input()

