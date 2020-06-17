letters = 'abcdefghijklmnopqrstuvwxyz'

backwards = letters[25::-1]
backwards = letters[::-1]

print(letters[16:13:-1])
print(letters[3-25::-1]) # edcba
print(letters[4::-1])
print(letters[25:25-8:-1]) # last 8 chars in reverse order
print(letters[:-9:-1])

print(letters[0])
print(letters[:1]) # is better to use this because it will not result in error when the string is empty