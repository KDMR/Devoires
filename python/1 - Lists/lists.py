# Defining some lists
names_human = ["Koorosh", "Morgane", "Pauline", "Justin", "Megan", "Till", "Marianna", "Borin", "Katherine", "Lee", "Anastasia", "Shyam", "Salona"]
names_cars = ["Bugatti", "BMW", "Peykan", "Renault", "Mercedes-Benz", "Peugeot", "Citroen", "Alpine"]
names_computers = ["Altaire 8800", "IBM 610", "Kenbak-1", "MIR", "Datapoint 202", "Simon", "Micral N"]



### Printing the names of humans
# print("\n")
# print("Some human names are printed below :")
# print("------------------------------------")
# for name in names_human:
# 	print(name)



### Printing the names of some early time computers
# print("\n")
# print("Some old time's computer names are printed below :")
# print("------------------------------------------------")
# for name in names_computers:
# 	print(name)



### Printing the names of cars
# print("\n")
# print("Some recent car names are printed below :")
# print("-----------------------------------------")
# for name in names_cars:
# 	print(name)



### Insert into the end (right side) of the lists in Python
# print("\n")
# names_human.append("Issau")
# print("The new list of human names is:")
# print(names_human)



### Insert into the beginning (left side) of the lists in Python
# print("\n")
# names_human.insert(0, "Konrad")
# print("The new list of human names is:")
# print(names_human)



### Insert a name into the index 3 (fourth element of the list)
# print("\n")
# names_human.insert(3, "Courage")
# print("The new list of human names is:")
# print(names_human)



### Removing an item from the end of list using the pop() method
# popped_name = names_human.pop()
# print("Last item of the list (popped one) is:")
# print(popped_name)
# print("The list is now like:")
# print(names_human)



### Removing an item by it's index number
# popped_name = names_human.pop(0)
# print("Last item of the list (popped one) is:")
# print(popped_name)
# print("The list is now like:")
# print(names_human)



### Removing an item by it's value
# names_human.remove("Koorosh")
# print("The list is now like:")
# print(names_human)
# print("\n")



### Sorting a list permanantly
# names_human.sort()
# print(names_human)



### Printing a sorted form of a list
### withought changing the list itself
# print(sorted(names_human))



### Sorting a list in the reverse order
### First method:
		# names_human.sort(reverse=True)
		# print(names_human)
### Second method:
		# names_human.reverse()
		# print(names_human)



### Printing a reversed form of a list withought actually changing it:
### The reversed() function returns the reversed iterator of the given sequence.
### You therefore need to convert it to a list to be able to print it properly.
### reversed_names_human = list(reversed(names_human))
# print(reversed_names_human)



### Printing the length of a list
# print(len(names_human))



### Printing all values located in a list
# for name in names_human:
# 	print(name)



### Create a numerical list (like C languag's for-loop)
# for number in range(0, 10):
# 	print("Current Number: {0}".format(number))



### Printing all the members of a list
# for name in names_computers:
# 	print(name.title())



### Printing a list of decimal numbers
# for number in range(0, 10):
# 	print("Current Number: {0}".format(number))



### Make a list of numbers
# number_list = range(0, 21)
# print(number_list)



### On how to use the list comprehentions
### list comprehentions help you to use a
### for-loop, make some processing on the 
### data and then place them in a list all 
### by itself. These operations are done 
### along one line of code only.
# product_tax = 0.27
# product_price = [27, 34, 43, 77, 66.4, 89.5, 55]
# values = [price*product_tax + price for price in product_price]
# for value in values:
#   print("The total price for you to pay is: {0}$ .".format(value))



### Slicing a list
### in slicing a list, the first number is the index to start from
### the second number is where to end and the third one is the stps
### to be taken. If any of the numbers are not written, the maximum
### number possible will be considered to be taken into accout.
### Example_1:
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print (my_list[-1:-6:-1])
### Example_2:
# my_list = range(0, 21)
# print(my_list[0::2])



### On how to loop throught a slice
# new_wishes = ["I wish that {0} was not this expensive.".format(car_name) for car_name in names_cars]
# for wish in new_wishes[:4]:
# 	print(wish)































##############################################
## I Am On Line: 148 of Python_Crash_Course ##
##############################################









#################################################################################
#################################################################################
#################################################################################
