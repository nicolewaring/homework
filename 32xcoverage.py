# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below


"""
python3 32xcoverage.py 10 10 1
5 20 10.82375
"""

import sys
import random

size = int(sys.argv[1])
number = int(sys.argv[2])
length = int(sys.argv[3])

Sum = 0

List = [0] * size



Max = 0 


for i in range (number):
	ind = random.randint(0,size - length)
	for j in range (length):
		List[ind] += 1 
		ind = ind + 1
	
for i in List:
	if i > Max:
		Max = i 
		
Min = List[length]

for i in List[length:size - length]:
	if i < Min:
		Min = i
	

for i in List:
	Sum += i 
	print(Sum)

print(Min, Max, Sum/(size))