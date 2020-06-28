with open("binary","bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))
    # bin_file.write(bytes(range(17))
with open("binary","br") as bin_file:
    for b in bin_file:
        print(b)