#!/usr/bin/python3
#/////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////  Dictionaries   ///////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////

nest_list = []
nest_dict = {}
user1_info = {"fname":"Grace", "lname":"Hopper"}
user2_info = {"fname":"mike", "lname":"Muuss"}
user3_info = {"fname":"Dennis", "lname":"Ritchie"}
user4_info = {"fname":"Ken", "lname":"Thompson"}
car = {"Window": 4, "Wheel": 4, "Antenna": 1, "Wheel": 40}



### On how a dictionaty is
# user1_info = {"fname":"Grace", "lname":"Hopper"}
# user2_info = {"fname":"mike", "lname":"Muuss"}
# user3_info = {"fname":"Dennis", "lname":"Ritchie"}
# user4_info = {"fname":"Ken", "lname":"Thompson"}
# print("User_1's first name is: " + user1_info["fname"])
# print("User_1's last name is: " + user1_info["lname"])
# print("User_1's first name is: " + user2_info["fname"])
# print("User_1's last name is: " + user2_info["lname"])



### How to add new elements to dictionary
# car = {"Window": 4, "Wheel": 4}
# car["Antenna"] = 1
# print(car)



### How to modify a value in a dictionary
# car = {"Window": 4, "Wheel": 4}
# car["Wheel"] = 6
# print(car)



### How to delete a key-value pair
# car = {"Window": 4, "Wheel": 4, "Antenna": 1}
# print("The current state of the car is: " + str(car))
# del car["Antenna"]
# print("The current state of the after some deletion is: " + str(car))



### How to loop throught all key-value pairs
# car = {"Window": 4, "Wheel": 4, "Antenna": 1}
# for key, value in car.items():
# 	print("\nNumber of {0}s: {1}".format(key, value))



### Looping throught the keys of a dictionary
# for key in user1_info.keys():
# 	print("\n{0}".format(key))



### Looping throught a dictionariy's keys in order
# print("Ordered list of keys:")
# for key in sorted(car.keys()):
# 	print("\t{0}".format(key))



### How to loop throught all values of a dictionary
# for value in car.values():
# 	print("value is: {0}.\n".format(value))



### How to do Nesting
### If you place some dictionaries or lists inside 
### another dictionay or another list, your are 
### nesting them. Below are some examples:



### nesting dictionaries inside a list
# nest_dict = [user1_info, user2_info]
# print(nest_dict)



## nesting dictionaries inside a dictionary
# store_available_cars = {
# 	"BMW" : {
# 		"BMW 7 Series" : 2,
# 		"BMW 8 Series" : 1,
# 		"BMW M5" : 5,
# 		"BMW i8" : 2
# 	},
# 	"Renault" : {
# 		"Renault Zoe" : 3,
# 		"Renault Kiger" : 2,
# 		"Renault K-ZE" : 2,
# 		"Renault Arkana" : 1
# 	}
# }
# for brand, model in  store_available_cars.items():
# 	for name, number in model.items():
# 		print("Brand: {0}\n\tModel: {1}\n\tNumber available:{2}\n\t".format(brand, name, number))



