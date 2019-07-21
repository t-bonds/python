#Sam Lyons
#CIS-294
#4/7/19
#Assignment 9

"""A program that calculates
and displays grades.."""

grades = [100, 93, 87, 72, 100, 64, 56, 95, 85]

def print_grades(grades_input):
	for grade in grades_input:
		print(grade) 

def grades_sum(scores):
	total = 0
	for score in scores:
		total += score
	return total
	
def grades_average(grades_input):
	sum_of_grades = grades_sum(grades_input)
	average = sum_of_grades / float(len(grades_input))
	return average

def grades_variance(grades):
	variance = 0
	for number in grades:
		variance += (grades_average(grades) - number) ** 2
	return variance / len(grades)
	
def grades_std_deviation(variance):
	return variance ** 0.5


variance = grades_variance(grades)	
print_grades(grades)
print("Sum: " + str(grades_sum(grades)))
print("Average: " + str(grades_average(grades)))
print("Variance: " + str(variance))	
print("Std. Div.: " + str(grades_std_deviation(variance)))			