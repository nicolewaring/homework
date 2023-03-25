# 50dust.py

#!/usr/bin/env python3

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)


"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGCTTTTcATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTaaaaaaaGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGAGTAAattaaaattttATTGACTTAGG
TCACTAAATacTTTAACCAATATAGGCATAGCGCACAGACAGAtAaaaaTTACAGAGTAC
ACAacATCCATGAAACGCATTAGCACCACCATTACCAccaccatCACCATTACCACAGGT
AACGGTGCgGGCTGACGCGTACAGGAAACacagaaaaAAGCCCGCACCTGACAGTGCGGG
CTttttttTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AGGCAGggGCaGGTGGCCACCGTCcTCtctgcccCcgcCAAAatcaccaacCACCTGGTG
GCGATGATTGaAAAAacCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA

Timings
win alg1 alg2
11  28.7 25.8
25  30.4 26.1
100 33.2 26.1
200 37.4 25.9
"""

import argparse 
import mcb185
import math

import os

parser = argparse.ArgumentParser(description='Fasta File Entropy Filtering')

#positional argument
parser.add_argument('file', type =str, metavar='file', help='fasta file')

#optional arguments with default parameters
parser.add_argument('-w', required=False, type=int, default=11)
parser.add_argument('-t', required=False, type=float, default=1.4)

#switches
parser.add_argument('-s', action='store_true',
	help = 'N-based masking')
	
	
arg = parser.parse_args()

window = arg.w
threshold = arg.t

def ShanEnt(seq):
	SE_sum = 0
	for nt in 'ACGT':
		SE_val = seq.count(nt)/len(seq)
		if SE_val != 0:
			SE_sum += SE_val * ((math.log((1/SE_val), 2)))
	return SE_sum
	
for defline, seq in mcb185.read_fasta(arg.file):
	words = defline.split('>')
	name = words[0]
	
	seq = seq.upper()
	
	lseq = list(seq)
		
	for i in range(len(seq) - arg.w+1):	
		win = seq[i:i+arg.w]
		if ShanEnt(win) < arg.t:
			for j in range(i, i+arg.w):
				if arg.s:
					lseq[j] = lseq[j].lower()
				else:
					lseq[j] = 'N'
	seq = "".join(lseq)
	print(f">{name}")
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])