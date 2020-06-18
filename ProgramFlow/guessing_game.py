import random
answer = random.randint(1, 10)
print(answer)
# answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())
count = 1
while(guess != answer):
    if guess == 0:
        break
    elif guess < answer:
        print("Please guess higher")
        count += 1
    elif guess > answer:
        print("Please guess lower")
        count += 1
    guess = int(input())
if guess != 0:
    print("You got it right the {} times".format(count))
