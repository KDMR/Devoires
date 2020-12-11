#!/usr/bin/python3
#/////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////  Dictionaries   ///////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////

names_human = ["Koorosh", "Morgane", "Pauline", "Justin", "Megan", "Till", "Marianna", "Borin", "Katherine", "Lee", "Anastasia", "Shyam", "Salona", "Estragon", "Vladimir", "Pozzo", "Godot", "Lucky", "Gary"]
names_artists = {"janis joplin": "singer", "william turner": "painter", "pier paolo pasolini": "film director"}
names_cars = ["Bugatti", "BMW", "Peykan", "Renault", "Mercedes-Benz", "Peugeot", "Citroen", "Alpine"]
names_computers = ["Altaire 8800", "IBM 610", "Kenbak-1", "MIR", "Datapoint 202", "Simon", "Micral N"]
user1_info = {"fname":"Grace", "lname":"Hopper"}
user2_info = {"fname":"mike", "lname":"Muuss"}
user3_info = {"fname":"Dennis", "lname":"Ritchie"}
user4_info = {"fname":"Ken", "lname":"Thompson"}
car = {"Window": 4, "Wheel": 4, "Antenna": 1, "Wheel": 40}



### How is a function written and called?
# def welcome():
# 	for name in names_human:
# 		print("Hello {0} and welcome!".format(name))
# welcome()



### How to pass information to a function
# def welcome(name):
# 	print("Hello {0} and welcome!".format(name))
# for name in names_human:
# 	welcome(name)



### How to use positional arguments
# name = "Estragon"
# car = names_cars[0]
# def friends_news(name, car):
# 	print("{0} has just bought a new {1}.".format(name.upper(), car.upper()))
# friends_news(name, car)



### What are keyword arguments?
### You do not need to pass keyword arguments in order
# name = "Estragon"
# car = names_cars[0]
# def friends_news(person_name, person_car):
# 	print("{0} has just bought a new {1}.".format(name.upper(), car.upper()))
# friends_news(person_name = name, person_car = car)



### How to use default values for arguments?
# def animal_care(name, action = "Feeding"):
# 	print("Action to be taken on {0} is: {1}.".format(name, action))
# animal_care("Puppy", "Grooming")
# animal_care("caty")
# animal_care("Piggy", "Washing")



### How does retutn value work in python?
# def artist(name, style):
# 	artist_description = name.title() + " was a " + style.title() + "."
# 	return artist_description
# for name, style in names_artists.items():
# 	result = artist(name, style)
# 	print(result)



### Pass a list to a function
### In this way, by making any changes to the username list,
### the original names_human will also change
# names = names_human
# def greet_users(names):
# 	for name in names:
# 		msg = "Hello, " + name.title() + "!"
# 		print(msg)
# greet_users(names)



### Pass a list to a function without changing
### the original list at later times by passing a copy of it
### a copy of it to the function
# names = names_human[:]
# def greet_users(names):
# 	for name in names:
# 		msg = "Hello, " + name.title() + "!"
# 		print(msg)
# greet_users(names)



### Passing an unknown number of arguments
# def account(*payments):
# 	transactions = []

# 	"""Receiving the list of transactions"""
# 	for payment in payments:
# 		transactions.append(payment)
	
# 	"""Calculating the account's balance"""
# 	balance = 0
# 	for amount in transactions:
# 		balance += amount
	
# 	"""Printing the list of transactions"""
# 	print("The list of incomes and payments: ")
# 	for transaction in transactions:
# 		print("\t{0}".format(transaction))

# 	"""Printing the balance"""
# 	print("\nThe balance of your account:\n\t{0}$\n".format(balance))

# account(27000, 30000, -26000)




### How to put a function in a module and call it
### the modules.py is include in the same folder
# import modules
# name = "Zaza"
# modules.greet_people(name)


### What is a .pyc file
###   This description comes from the link below:
###   https://www.tutorialspoint.com/What-are-pyc-files-in-Python
# .pyc files are created by the Python interpreter when a .py file is imported.
# They contain the "compiled bytecode" of the imported module/program so that
# the "translation" from source code to bytecode (which only needs to be done once) 
# can be skipped on subsequent imports if the .pyc is newer than the corresponding .py file,
# thus speeding startup a little. But it's still interpreted. 
# Once the *.pyc file is generated, there is no need of *.py file, unless you edit it.



### How to correctly call a function that is written in a module
# WHEN IMPORTING, CONSIDER THE FACT THAT IMPORTING THE ENTIRE MODULE IS DONE BY IMPORTING
# ITS FILENAME. THIS MODULE MIGHT CONTAIN A METHOD AS THE NAME AS THE MODULE ITSELF. 
# AS A RESULT, DO NOT FORGET TO USE THE METHOD AS THE FOLLOWING WAYS:
# 1)	If importing the whole method:
# 		Example:
# 		import pprint
# 		pprint.pprint(myDict)
# 2)	If importing the method from module:
# 		Example:
# 		from pprint import pprint
# 		pprint(myDict)



### How to use `as` to give a function an alias
import modules as m
name = "Zaza"
m.greet_people(name)