import csv

name = input("what's your name? ")
home = input("where's your home? ")

with open("add.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["home","name"])
    writer.writerow({"name":name,"home":home})


