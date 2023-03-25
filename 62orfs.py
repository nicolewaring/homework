# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome


"""

NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""

import argparse 
import mcb185 

parser=argparse.ArgumentParser(description="Finds ORF's in E.coli Genome")

#positional argument 
parser.add_argument('file', type=str, metavar='file', help='fasta file')

#optional arguments with default parameters
parser.add_argument('-m', required=False, type=int, default= 300, metavar='ORF size', 
	help='ORF size')

arg=parser.parse_args()

for defline, seq in mcb185.read_fasta(arg.file):
	neg=mcb185.revcomp(seq)
	
	seqs=[seq]

	
	for strand in seqs:
		for frame in range(3):
			in_ORF=False
			for j in range(frame, len(seq), 3):
				codon=mcb185.translate(seq[j:j+3])
				if codon=='M' and not in_ORF:
					in_ORF=True
					startcoord=j
					
				if in_ORF and codon=='*':
					cds=mcb185.translate(strand[startcoord:j+3])
					if len(cds)>arg.m:
						print(defline, startcoord+1, j+3, '+', cds[:10])		

	negs=[neg]
	for strand in negs:
		for frame in range(3):
			in_ORF=False
			for j in range(frame, len(seq), 3):
				codon=mcb185.translate(seq[j:j+3])
				if codon=='M' and not in_ORF:
					in_ORF=True
					startcoord=j
					
				if in_ORF and codon=='*':
					cds=mcb185.translate(strand[startcoord:j+3])
					if len(cds)>arg.m:
						print(defline, len(seq)-startcoord +1, len(seq)-j+3, '-', cds[:10])
	
		
	