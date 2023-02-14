# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list


"""
python3 33birthday.py 365 23
0.571
"""

import sys
import random

days = int(sys.argv[1])
people = int(sys.argv[2])

trials = 10000

#calendar a list
TrueSum = 0
calendar = [0] * days

for i in range(trials):
	for i in range(people):
		bday = random.randint(0,days - 1)
		calendar[bday] += 1
    

	for i in range(len(calendar)):
		if calendar[i] > 1:
			success = True
			break  
		else:
			success = False

	if success == True:
		TrueSum += 1 

	
	calendar = [0] * days
    	
print(TrueSum/trials)


#birthdays a list 

TrueSum = 0
birthdays = []
samebd = []
for i in range(trials):
	for i in range(people):
		bday = random.randint(0, days - 1)
		birthdays.append(bday)
		
	for j in birthdays:
		if j not in samebd:
			samebd.append(j)
		else:
			success = True
			TrueSum += 1 
			break 
	
	
	birthdays = []
	samebd = []

print(TrueSum/trials)
		

		

