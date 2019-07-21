#Sam Lyons
#CIS-294
#4/28/19
#Assignment 12

"""A program that utilizes File
Input and Output."""

name = "Sam Lyons" #variable declaration
fileAssign = "Programming Assignment 12"

print("Write to file: ")

file = open("assign12.txt", "w+") #opens and writes to file
file.write(name + "\n" + fileAssign)

check = False
print("Closed: "+ str(check))
file.close()
if file.closed:
    check = True
print("Closed: "+ str(check))

print("Read from file: ")
file1 = open("assign12.txt", "r")
print(file1.read())
file1.close()
print("\nRead from file line by line:")
file2 = open("assign12.txt", "r")
print(file2.readline())
print(file2.readline())
file.close()
