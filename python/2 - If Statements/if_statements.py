# Defining some lists
names_human = ["Koorosh", "Morgane", "Pauline", "Justin", "Megan", "Till", "Marianna", "Borin", "Katherine", "Lee", "Anastasia", "Shyam", "Salona"]
names_cars = ["Bugatti", "BMW", "Peykan", "Renault", "Mercedes-Benz", "Peugeot", "Citroen", "Alpine"]
names_computers = ["Altaire 8800", "IBM 610", "Kenbak-1", "MIR", "Datapoint 202", "Simon", "Micral N"]



# how to write an if (example 1)
name = "Shirin"
list_name = "names_human"
if name in names_human:
	print("{0}is in the list: names_human".format(name))
else:
	print("{0} is not in the list: {1}".format(name, list_name))