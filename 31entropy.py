# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""

import math 
import sys


list =[]
for value in sys.argv[1:]:
	try:
		list.append(float(value))
	except:
		raise ValueError(f'One or more inputted values not a number.')

try:
	assert(math.isclose(sum(list), 1.0))
except:
		raise ValueError(f'Sum of inputted values does not add to 1.0.')
		
SE_sum = 0
for value in list:
	SE_sum += (value) * ((math.log((1/value), 2)))
	

print (round(SE_sum, 3))