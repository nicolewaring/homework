# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane


"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""

import mcb185
import gzip
import os 

home = os.getenv('HOME')
print(home)

prot = 'DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz'

def KD(seq):
	sumKD = 0
	for j in seq:
		if j == 'I':
			sumKD += 4.5 
		if j == 'V':
			sumKD += 4.2 
		if j == 'L':
			sumKD += 3.8
		if j == 'F':
			sumKD += 2.8
		if j == 'C':
			sumKD += 2.5 
		if j == 'M':
			sumKD += 1.9 
		if j == 'A':
			sumKD += 1.8 
		if j == 'G':
			sumKD -= 0.4
		if j == 'T':
			sumKD -= 0.7
		if j == 'S':
			sumKD -= 0.8
		if j == 'W':
			sumKD -= 0.9
		if j == 'Y':
			sumKD -= 1.3 
		if j == 'P':
			sumKD -= 1.6
		if j == 'H':
			sumKD -= 3.2
		if j == 'E':
			sumKD -= 3.5
		if j == 'Q':
			sumKD -= 3.5
		if j == 'D':
			sumKD -= 3.5
		if j == 'N':
			sumKD -= 3.5
		if j == 'K':
			sumKD -= 3.9
		if j == 'R':
			sumKD -= 4.5
	return sumKD/len(seq)
	
def hyd(seq, w, t):
	for i in range(len(seq) - w + 1):
		win = seq[i: i+w]
		if KD(win) > t and 'P' not in win:
			return True
	return False

for defline, seq in mcb185.read_fasta(f'{home}/{prot}'):
	words = defline.split()
	name = words[0]
	#split sequence into first 30AA and the rest
	nterm = seq[0:30]
	cterm = seq[30:]
	if hyd(nterm, 8, 2.5) and hyd(cterm, 11, 2.0):
		print(name, defline)