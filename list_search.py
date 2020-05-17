# Lists are ordered and changable. Lists allow duplicate members
#list operation to check for an item in the list
import re

names = ['Aditya','Nisar','Akshay','Suhas','Ashish']

nm = input("Enter a name: ")
if not re.match("^[A-Z][a-z]*$", nm):
    print("Please enter a string")

if nm in names:
    print(nm,"is in the list.")
else:
    print(nm,"is not in the list")
