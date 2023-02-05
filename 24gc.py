# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'


"""
python3 24gc.py
0.42
"""
sumGC= 0
for i in range(len(dna)):
	if dna[i] == "G" or dna[i] == "C":
		sumGC = sumGC + 1 
answer = sumGC/len(dna)

print(f'{answer:.2f}')
		
		