#Sam Lyons
#CIS-294
#4/14/19
#Assignment 10

"""A program that uses Advanced Topics
in the Python Programming Language."""

myInfo = {						#dictionary containing personal information
	"First Name": "Sam",
	"Last Name": "Lyons",
	"Age": 20,
	"Occupation": "Arby's Heir",
}

print("Items: " + str(myInfo.items())) #printing of dictionary
print("Keys: " + str(myInfo.keys()))
print("Values: " + str(myInfo.values()))
print("137 in binary: " + bin(137))		#number conversion
print("64 in octal: " + oct(64))
print("234 in hexadecimal: " + hex(234))
print("0b1101 in decimal: " + str(0b1101))

fives = [x for x in range(0,31) if x % 5 == 0] #multiples of five
print("Multiples of 5: " + str(fives))

name = str(myInfo["First Name"] + " " + myInfo["Last Name"]) #name backwards only evens
print("Name Backwards Only Evens: " + name[::-2] )


print("Evens With Lambda: " + str(map(lambda x: x * 2, range(0,11))))




