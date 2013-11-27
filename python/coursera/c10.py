import sys
from util import dna2rna, rna2protein, reverseComplement


def findProtein(dna, p):
    window_len = len(p) * 3
    dna_len = len(dna)
    if dna_len < window_len:
        sys.exit()
    for i in range(0, dna_len - window_len + 1):
        d = dna[i:i + window_len]
        if rna2protein(dna2rna(d)) == p:
            print d
        elif rna2protein(dna2rna(reverseComplement(d))) == p:
            print d


if __name__ == '__main__':
    dna = raw_input()
    p = raw_input()

    findProtein()
