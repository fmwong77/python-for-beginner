string = "Python is a very powerful language"
vowels = frozenset("aeiou")
result = set()

for char in string:
    if char not in vowels:
        result.add(char)

final = set(string).difference(vowels)
print(final)
print(sorted(final))