# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list


"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""

import gzip 
import sys 

sumA = 0
sumC = 0
sumD = 0
sumE = 0
sumF = 0
sumG = 0
sumH = 0
sumI = 0
sumK = 0
sumL = 0
sumM = 0
sumN = 0
sumP = 0
sumQ = 0
sumR = 0
sumS = 0
sumT = 0
sumV = 0
sumW = 0
sumY =0
total = 0 

with gzip.open(sys.argv[1], 'rt') as fp: 
	for line in fp.readlines():
		if line.startswith(">"):
			continue
		for char in line:
			total += 1
			if char == 'A':
				sumA += 1
			elif char == 'C':
				sumC += 1
			elif char == 'D':
				sumD += 1
			elif char == 'E':
				sumE += 1
			elif char == 'F':
				sumF += 1
			elif char == 'G':
				sumG += 1
			elif char == 'H':
				sumH += 1
			elif char == 'I':
				sumI += 1 
			elif char == 'K':
				sumK += 1
			elif char == 'L':
				sumL += 1
			elif char == 'M':
				sumM += 1
			elif char == 'N':
				sumN += 1
			elif char == 'P':
				sumP += 1
			elif char == 'Q':
				sumQ += 1
			elif char == 'R':
				sumR += 1
			elif char == 'S':
				sumS += 1 
			elif char == 'T':
				sumT += 1
			elif char == 'V':
				sumV += 1 
			elif char == 'W':
				sumW += 1
			elif char == 'Y':
				sumY += 1
print('A', sumA, round(sumA/total, 4))
print('C', sumC, round(sumC/total, 4))
print('D', sumD, round(sumD/total, 4)
print('E', sumE, round(sumE/total, 4))
print('F', sumF, round(sumF/total, 4))
print('G', sumG, round(sumG/total, 4))
print('H', sumH, round(sumH/total, 4))
print('I', sumI, round(sumI/total, 4))
print('K', sumK, round(sumK/total, 4))
print('L', sumL, round(sumL/total, 4))
print('M', sumM, round(sumM/total, 4))
print('N', sumN, round(sumN/total, 4))
print('P', sumP, round(sumA/total, 4))
print('Q', sumQ, round(sumQ/total, 4))
print('R', sumR, round(sumR/total, 4))
print('S', sumS, round(sumS/total, 4))
print('T', sumT, round(sumT/total, 4))
print('V', sumV, round(sumV/total, 4))
print('W', sumW, round(sumW/total, 4))
print('Y', sumY, round(sumY/total, 4))




#list variation

s = 'ACDEFGHIKLMNPQRSTVWY'
l = 20 * [0]
total = 0 
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp.readlines():
		if line.startswith(">"):
			continue
		print(line)
		for char in line:
			total += 1 
			for i in range(len(s)):
				if s[i] == char:
					l[i] += 1
					continue 
for j in range(len(l)):
	print(s[j], l[j], round(l[j]/total, 4))
		
		
		
		
		
#string method - find/index methods 

					


						