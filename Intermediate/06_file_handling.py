#File Handling

import os

# .txt file

txt_file = open("Intermediate/my_file.txt", "r+") #Leer y escribir
#print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)
    
#txt_file.write("\nAunque tambien me gusta JavaScript") #Ayuda a escribir en el fichero
#print(txt_file.readline())

#.json file

import json

json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name":"José", 
    "surname":"Odé",
    "age":35,
    "languages":["Python", "Java", "C#"],
    "website": "https://jose.ode"}

json.dump(json_test, json_file, indent= 4)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

#.csv file

import csv

csv_file = open("Intermediate/my_file.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["José", "Odé", "32", "Python", "https://jose.ode"])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

#.xlsx file

#import xlrd # Debe instalarse el módulo

#.xml file

import xml