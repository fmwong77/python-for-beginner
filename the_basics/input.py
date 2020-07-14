first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
print(f"Hello {first_name} {last_name}")
print("Hello %s %s" % (first_name, last_name))

def foo(name):
    return "Hi %s%s" % (name[0].upper(), name[1:len(name)])

print(foo("mary"))

string = "Hello"
for char in string:
  print(char.title())