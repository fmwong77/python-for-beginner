# cities = ["Adelaide","Alice Springs","Darwin","Melbourne","Sydney"]
# with open("original.txt","w") as cities_file:
#     for city in cities:
#         print(city, file=cities_file)

# cities = []
# with open("original.txt","r") as city_file:
#     for city in city_file:
#         cities.append(city.strip())
# print(cities)
# for city in cities:
#     print(city)

# imelda = "More Mayhem", "Imelda Mayhem", 2011, ((1,"Pulling the Rug"), (2,"Psycho"),(3,"Mayhem"),(4,"Kentish Town Waltz"))
# with open("imelda3.txt","w") as imelda_file:
#     print(imelda, file=imelda_file)

with open("imelda3.txt","r") as imelda_file:
    content = imelda_file.readline()
imelda = eval(content)
print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)