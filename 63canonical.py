# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein


"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""

import gzip 
import re 
import argparse

parser = arg.parse.ArgumentParrser(description'Repeats Start Codons From E. coli Genome')
parser.add_argument('file', type=str, metavar='<path>', help='genomic file')
arg=parser.parse_args()

#ignore pseudogenes
with gzip.open(arg.file, 'rt') as fp:
	for line in fp:
		if line.startswith('ORIGIN'):
			break
		for line in fp:
			f=line.split()
			sequence += "".join(f[1:])

with gzip.open(arg.file, 'rt') as fp:
	for line in fp.readlines():
		for match in re.finditer('\s(CDS)\s', line):
			coordinate=re.search('\d+)\.\.(\d+)', line)
			start=coor.group(1)
			end=coor.group(2)
			
			print(sequence[beg-1:beg+2])
			#if i in line:
				#print(line, start)