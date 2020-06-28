# jabber = open("original.txt", "r")
# for line in jabber:
#     if "challenge time" in line.lower():
#         print(line, end='')
#         # print(line)
# jabber.close()

# with open("original.txt", "r") as jabber:
#     for line in jabber:
#         if "challenge time" in line.lower():
#             print(line, end='')
#

# using readline()
# with open("original.txt","r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# using readlines(), returned as list
with open("original.txt","r") as jabber:
    lines = jabber.readlines()
print(lines)
for line in lines[::-1]:
    print(line, end='')

print("*" * 40)
# using read(), returned as string
with open("original.txt","r") as jabber:
    lines = jabber.read()
print(lines)
for line in lines[::-1]:
    print(line, end='')
