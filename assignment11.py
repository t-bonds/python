#Sam Lyons
#CIS-294
#4/21/19
#Assignment 11

"""A program that uses Object Oriented Programming
in the Python Programming Language."""

class Car(object): # class for Car Object
	condition = "new"
	miles = 0
	def __init__(self, make, model, year, color):
		self.make = make
		self.model = model
		self.year = year
		self.color = color

	def __repr__(self):
		return ("This is a %s %s %s %s in %s condition with %s miles." % (self.color, self.year, self.make, self.model, self.condition, self.miles))	


	def drive_car(self, miles):
		self.condition = "used"
		self.miles = miles

class SUVCar(object): #class for SUV Car Object
	def __init__(self, make, model, year, color, options):
		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.options = options

	def __repr__(self):
		return ("This is a %s %s %s %s in %s condition with %s miles and %s" % (self.color, self.year, self.make, self.model, self.condition, self.miles, self.options))	

	def drive_car(self, miles):
		self.condition = "used"
		self.miles = miles


		
my_car = Car("Nissan", "Altima", 2013, "silver") #declares my_car variable
my_SUV = SUVCar("Toyota", "Forerunner", 2009, "black", "Rear-View Camera")
print(my_car)	
my_SUV.drive_car(32500)
print(my_SUV)	
		

