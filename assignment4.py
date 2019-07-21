#Sam Lyons
#CIS-294
#2/17/19
#Assignment 4

"""A program that returns values pertaining to a vacation based on values
selected by the user."""


def hotel_cost(nights): #calculates the total cost of the hotel depending on the number of nights stayed.

	return 140 * nights


def plane_ride_cost(city): #calculates the cost of the plane ride depending on the destination.

	if city == "Charlotte":

		return 183

	elif city == "Tampa":
	
		return 220

	elif city == "Pittsburgh":
	
		return 222

	elif city == "Los Angeles":
	
		return 475

def rental_car_cost(days): #calculates the cost of the rental car depending on the number of days intended.

	cost = days * 40

	if days >= 7:

		cost -= 50

	elif days >= 3:
	
		cost -= 20

	return cost
	
def trip_cost(city, days, spending_money): #function that concatenates all values into a single return statement.

	print ("Rental Cost: " + str(rental_car_cost(days)) 
	+ "\nHotel Cost: " + str(hotel_cost(days))
	+ "\nPlane Ride Cost: " + str(plane_ride_cost(city))
	+ "\nSpending Money: " + str(spending_money))



trip_cost("Pittsburgh", 12, 1200)	#determines the inputs of all functions and then prints them to the console.	






