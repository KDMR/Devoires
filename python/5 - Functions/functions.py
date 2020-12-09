#!/usr/bin/python3
#/////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////  Dictionaries   ///////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////

names_human = ["Koorosh", "Morgane", "Pauline", "Justin", "Megan", "Till", "Marianna", "Borin", "Katherine", "Lee", "Anastasia", "Shyam", "Salona", "Estragon", "Vladimir", "Pozzo", "Godot", "Lucky", "Gary"]
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



