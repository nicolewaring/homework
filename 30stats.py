# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys


"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""

import sys 

list = []

for value in sys.argv[1:]:
	
	list.append(int(value))

#calculating Count option 1 
count1 = 0
for num in list:
	count1 += 1
	
print("Count:", count1)


#calculating Minimum
list.sort()
minimum = list[0]
print("Minimum:",f'{minimum:.1f}')

#calculating Maximum
list.sort()
maximum = list[-1]
print("Maximum:",f'{maximum:.1f}')

#calculating Mean
mean_sum = 0
for num in list:
	mean_sum += list[num-1]
	mean = mean_sum / len(list)
print("Mean:",f'{mean:.3f}')

#calculating Standard Deviation
sd_sum = 0
for num in list:
	dist = list[num-1] - mean
	sd_sum += (dist ** 2)
sd = (sd_sum / len(list))** 0.5
print("SD:",f'{sd:.3f}')

#calculating Median
list.sort()
if len(list) % 2 == 0:
	
	median = (list[(len(list) // 2)] + list[(len(list) // 2) - 1] ) / 2
		
	
else:
	median = list[(len(list) // 2)]

print("Median:",f'{median:.3f}')