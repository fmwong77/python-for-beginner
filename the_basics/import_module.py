import time # built-in library
import os # standard library
import pandas # third party library

while True:
  if os.path.exists("files/temps_today.csv"):
    data = pandas.read_csv("files/temps_today.csv")
    print(data.mean())
    print(data.mean()["st1"])
  else:
    print("File does not exist.")
  time.sleep(10)
