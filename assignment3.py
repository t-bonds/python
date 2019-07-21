#Sam Lyons
#CIS-294
#2/10/19
#Assignment 3

"""A program in which the user enters their grade average, and the program
returns the letter grade to with the numerical value responnds to."""


def ranges(x):
	
	if x < 60 and x >= 0: #if/elif block that determines and prints the user's letter grade.

		print('You made a F!') 

	elif x < 70 and x >=60:

		print('You made a D!')

	elif x < 80 and x >=70:

		print('You made a C!')

	elif x < 90 and x >=80:

		print('You made a B!')

	elif x <= 100 and x >=90:

		print('You made an A!')

	else: 

		print('Error: You entered an invalid grade!')




def main():

	grade = 0
	print('Grade Calculator')
	print('\nEnter a grade as an integer (whole number):', end = ' ')
	grade = int(input()) #gets user input of their numerical grade.

	ranges(grade) #calls the ranges function with an input of the user's grade.

main()	

