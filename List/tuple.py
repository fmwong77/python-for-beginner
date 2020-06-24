welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda Day", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"))
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# metallica[0] = "Master of puppets"
# imelda = imelda[0], "Imelda May", imelda[2]
title, artist, year, track = imelda
print(title)
print(artist)
print(year)
print(track[0])

# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")]
print(imelda[0], imelda[1], imelda[2])
imelda[3].append((5, "Another Song"))
for song in imelda[3]:
    track, title = song
    print("\tTrack number {}, {}".format(track, title))
