
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



### Printing all the members of a list
# for name in names_computers:
# 	print(name.title())



### Printing a list of decimal numbers
# for number in range(0, 10):
# 	print("Current Number: {0}".format(number))



### Make a list of numbers
# number_list = range(0, 21)
# print(number_list)




























#################################################################################
#################################################################################
#################################################################################