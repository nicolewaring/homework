# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers


"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
import random 

length = 30
sumAT = 0
seq = ''
for i in range(length):
	r = random.randint(1, 10) # generate a random number from 1 to 4
	if   r < 4: 
		seq += 'A'
		#print('A', end='')
		sumAT += 1 
	elif r < 7: 
		#print('T', end='')
		seq += 'T'
		sumAT += 1
	elif r < 9: 
		#print('C', end='')
		seq += 'C'
	else:        
		#print('G', end='')
		seq += 'G'

print(length, sumAT / length, seq)