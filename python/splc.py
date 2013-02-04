from python.util import *

dna = input()
introns = []
while True:
    s = input()
    if not s: break
    introns.append(s)

for intron in introns:
    dna = dna.replace(intron, '')
print(rna2protein(dna2rna(dna)))