# def foo(char, filepath):
#   count = 0
#   with open(filepath) as myfile:
#     content = myfile.read()
#     for chr in content:
#       if chr == char:
#           count += 1
#   return count

# print(foo('a', 'sample.txt'))


# with open("sample.txt") as bear_file:
#   content = bear_file.read()
    
# with open("first.txt", "w") as first_file:
#   first_file.write(content[:90])

with open("data.txt", "a+") as data:
  data.seek(0)
  content = data.read()
  for i in range(2):
      data.write(content)

  

