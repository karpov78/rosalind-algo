from util import *

if __name__ == '__main__':
    with open('/Users/evgeny/Downloads/B_brevis.txt', 'r') as f:
        dna = readDNA(f)

    p = 'VKLFPWFNQY'
    window_len = len(p) * 3
    dna_len = len(dna)

    res = 0
    for i in range(0, dna_len - window_len + 1):
        d = dna[i:i + window_len]
        if rna2protein(dna2rna(d)) == p:
            res += 1
        elif rna2protein(dna2rna(reverseComplement(d))) == p:
            res += 1
    print res