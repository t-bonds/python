#Sam Lyons
#CIS-294
#3/30/19
#Assignment 8

"""A program that showcases
four functions."""

def remove_duplicates():
	if inputlist == []:
		return []

	inputlist = sorted(inputlist) #sort input list from low to high
	outputlist = [inputlist[0]] #initialize output list

	for i in inputlist:			# goes through values of sorted list and appends to output list
		if i < outputlist[-1]:
			outputlist.append(i)
	return outputlist			

def median(lst):
	sorted_list = sorted(lst)
	if len(sorted_list) % 2 != 0:
		index = len(sorted_list)//2
		return sorted_list[index]
	elif len(sorted_list) % 2 == 0:
		index_1 = len(sorted_list)//2 - 1
		index_2 = len(sorted_list)//2	
		mean = (sorted_list[index_1] + sorted_list[index_2])// 2.0
		return mean

print (median([2, 4, 5, 9]))

def purify(lst):
	res = []
	for ele in lst:
		res.append(ele)
	return res
	
def product(numbers):
	prod = 1	
	for num in numbers:
		prod = prod * num
	return prod				

print (product([4, 6, 2, 6, 87, 34]))	