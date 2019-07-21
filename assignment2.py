#Sam Lyons
#CIS-294
#2/4/19
#Assignment 2

"""A program in which the user enters their full name and age, and the program
returns these values, with the addition of the number of characters in the name,
the current date, and the current time."""

import datetime


def main() :

	firstName = "";
	lastName = "";
	fullName = "";
	userAge = "";

	print('Strings and Dates\n')

	print('Please Enter Your First Name:', end = ' ')
	firstName = input()

	print('Please Enter Your Last Name:', end = ' ')
	lastName = input()

	print('Please Enter Your Age:', end = ' ')
	userAge = str(input())

	fullName = "%s %s" % (firstName, lastName)
	fullNameSen = "%s %s" % ('Your full name is', fullName)
	charSen = "%s %s %s" % ("It is", str(len(fullName)), "characters long")

	curDateTime = datetime.datetime.now()
	dateSen = "%s %s/%s/%s." % ('Today\'s date is:', curDateTime.month, curDateTime.day, curDateTime.year)
	timeSen = "%s %s:%s:%s." % ('The time now is:', curDateTime.hour, curDateTime.minute, curDateTime.second)




	print("%s. %s." % (fullNameSen, charSen))
	print('The third character of your name is ' + fullName[2:3] + '.')
	print('Your age is ' + userAge + '. ')
	print(dateSen)
	print(timeSen)

main()



	



