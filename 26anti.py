# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'


"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""

print("with slice syntax:")
revcom = ''
for i in dna[::-1]:
	if i == 'A':
		revcom += 'T'
	elif i == 'C':
		revcom += 'G'
	elif i == 'G':
		revcom += 'C'
	else:
		revcom += 'A'
print(revcom)

print("with range function:")
revcom = ''
for i in range(len(dna)):
	if dna[i] == 'A':
		revcom = 'T' + revcom
	elif dna[i] == 'C':
		revcom = 'G' + revcom
	elif dna[i] == 'G':
		revcom = 'C' + revcom
	else:
		revcom = 'A' + revcom
print(revcom)
	
	
	