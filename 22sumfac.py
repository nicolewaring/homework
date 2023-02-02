# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library


"""
python3 22sumfac.py
5 15 120
"""

# computing running sum
n = 3
sum = 0
for i in range(n+1):
	sum = sum + i 
print(sum)
# factorial of n 

fac = 1
for i in range(1, n+1):
	fac = fac * i
print(fac)