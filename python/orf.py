import re

from python.util import *


START_CODON = 'AUG'

def getORFs(rna):
    res = set()
    for m in re.finditer(START_CODON, rna):
        frame = getFrame(rna[m.start():])
        if frame:
            res.add(frame)
    return res


dna = input()
rna = dna2rna(dna)

res = getORFs(rna)
res = res.union(getORFs(dna2rna(reverseComplement(dna))))

print('\n'.join(res))