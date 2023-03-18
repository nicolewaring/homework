# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)


"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""

import mcb185
import math 
import sys 

import os

window = int(sys.argv[2])
threshold = float(sys.argv[3])

def ShanEnt(seq):
	SE_sum = 0 
	for nt in 'ACGT':
		SE_val = seq.count(nt)/len(seq)
		if SE_val != 0:
			SE_sum += (SE_val) * ((math.log((1/SE_val), 2)))
	return SE_sum

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	words=defline.split('>')
	name=words[0]
	lseq = list(seq)
	for i in range(len(seq)-window + 1):
		win = seq[i:i+window]
		if ShanEnt(win) < threshold:
			for j in range(i, i + window):
				lseq[j] = 'N'
	seq = "".join(lseq)
	print(f">{name}")
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])