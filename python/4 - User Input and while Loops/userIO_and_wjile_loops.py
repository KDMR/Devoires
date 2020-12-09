#!/usr/bin/python3
#/////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////  User Input and while Loops   /////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////

names_human = ["Koorosh", "Morgane", "Pauline", "Justin", "Megan", "Till", "Marianna", "Borin", "Katherine", "Lee", "Anastasia", "Shyam", "Salona"]


### How does input function work?
### Whatever the user inputs is read as a string
# userInput = input("Hi, What is your name? ")
# print("Welcome " +  userInput + ", Nice to meet you!")



### How to recieve integer values from input function?
### The input function stores the date that you enter 
### as a string. To convert it to an integer, use the built-in int()
### function.
# userInput = input("Enter your payment amount: ")
# print("Your wage is: {0}$.".format(int(userInput)))



### What is a while loop?
# inflation_rate = 1
# while inflation_rate<6:
# 	print("Inflation rate is now: {0}% .".format(inflation_rate))
# 	inflation_rate += 1
# print("inflation rate is now: {}%. Time to find an extra job.".format(inflation_rate))



### What is aflag?
### We use a variable (and call it a flag), we set it
### to false whenever the continuation of application's
### needs to be halted, and when a check is done on 
### the flag's value, the process may be terminated if
### the flag's value is False.
# prompt = "\nPlease enter your name to continue,"
# prompt += "\nEnter 'quit' to end the program. "
# message = print(prompt)
# active = True  # varible `active` is the flag
# retry_step = 0
# while active:
# 	message = input(">>> ")
# 	if message == 'quit':
# 		print("Step: {0}".format(retry_step))
# 		print("\nYou typed `quit`, therefore the program stopped running.\n")
# 		active = False
# 	else:
# 		print("Step: {0}".format(retry_step))
# 		print(message + "\n")
# 		retry_step += 1



### How to break loop execution immiditely
### Use `break` to exit the loop at once
# prompt = "Enter your name: "
# active = True
# while active:
# 	name = input(prompt)
# 	if name not in names_human:
# 		prompt = "\n\nAre you sure you have enough crecentials for the name: {0}?"
# 		prompt += "\nExiting the program now...\n"
# 		print(prompt.format(name))
# 		break
# 	else:
# 		print("Welcome {0}, you have successfully logged in.\n")



### How to pass the current loop operations 
### withought executing any of the follwing 
### operations of the current loop step?
# max_limit = int(input("Enter a number: "))
# current_number = 0
# print("Below is the list of all the odd numbers between 0 and {0}:".format(max_limit))
# while current_number < max_limit:
# 	current_number += 1
# 	if current_number % 2 == 0:
# 		continue
# 	print(current_number)