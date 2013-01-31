from util import readFASTA, locate

ALPHABET = ['A', 'C', 'G', 'T']

__author__ = 'ekarpov'

def buildKmer(k):
    if k == 1:
        return ALPHABET
    else:
        suffixes = buildKmer(k - 1)
        res = []
        for c in ALPHABET:
            for x in suffixes:
                res.append(c + x)
        return res


k = 4
dna = readFASTA()
kmer = buildKmer(k)
result = [0] * len(kmer)
for i in range(len(kmer)):
    result[i] = len(locate(kmer[i], dna[1]))

print(' '.join([str(x) for x in result]))