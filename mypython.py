# Nicolas Sim CS 344 python exploration

#create 3 files in the same directory with 10 random characters from the 
#lower case alphabet (no spaces and newline at end) then print our files

#then print two random int on separate lines (1-42)
#then next line print the product

#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#https://stackoverflow.com/questions/22639587/random-seed-what-does-it-do
#https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python

import random
import string

# returns 10 characters in the lower case alphabet
def randomChars():
	random_str = ""
	for i in range(10):
		random_str += (random.choice(string.ascii_lowercase))
	return random_str


#random chars we print out and store into our files later
#print first then add newline for the file format
x = randomChars()
y = randomChars()
z = randomChars()
print(x)
print(y)
print(z)

x += "\n"
y += "\n"
z += "\n"


#don't need a seed for this situation
num1 = random.randint(1,42)
num2 = random.randint(1,42)

print(num1)
print(num2)
print(num1*num2)

#the random characters are now put into their respective files
f = open('file1.txt', 'w')
f.write(x)
f.close()

f = open('file2.txt', 'w')
f.write(y)
f.close()

f = open('file3.txt', 'w')
f.write(z)
f.close()