#!/usr/bin/python3


class Person:
	def __init__(self, fname, lname, phone, address):
		self.fname = fname
		self.lname = lname
		self.phone = phone
		self.address = address

		print("{0} {1} is residing at {2}.\nYou can contact him at {3}.".format(self.fname, self.lname, self.address, self.phone))


person = Person("Koorosh", "Sadeghi", "0098-99999", "Needle Park")
