import math


def reverseComplement(dna):
    lookup = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([lookup[c] for c in reversed(dna)])


def isReversePalindrome(s):
    return s == reverseComplement(s)


def gcContent(s):
    sum = 0
    for c in s:
        if c == 'C' or c == 'G':
            sum += 1
    return float(sum * 100) / len(s)


def calcMaxDNA(data):
    maxLabel = None
    maxGCContent = 0
    for l, dna in data.items():
        c = gcContent(dna)
        if c > maxGCContent:
            maxGCContent = c
            maxLabel = l
    return maxLabel


def readFASTA(f):
    label = None
    dna = ''
    while True:
        line = f.readline()
        if not line:
            return None if not label else (label, dna)
        if line[0] == '>':
            label = line
        else:
            dna += line.strip()


def readDNA(f):
    dna = ''
    while True:
        line = f.readline()
        if not line:
            return dna
        dna += line.strip()


def readDNAs():
    d = []
    label = None
    dna = ''
    while True:
        line = raw_input()
        if not line:
            if label:
                d.append((label, dna))
            return d
        if line[0] == '>':
            if label:
                d.append((label, dna))
            label = line
            dna = ''
        else:
            dna += line.strip()


def getHammingDistance(s, t):
    d = 0
    for i in range(0, len(s)):
        if s[i] != t[i]:
            d += 1
    return d


def locate(t, s):
    loc = []
    for i in range(0, len(s) - len(t) + 1):
        if t == s[i:i + len(t)]:
            loc.append(i + 1)
    return loc


def printList(s):
    first = True
    res = ''
    for a in s:
        if not first:
            res += ' '
        res += str(a)
        first = False
    return res


class ProfileMatrix:
    def __init__(self, s):
        self.profile = {'A': ([0] * len(s)), 'C': ([0] * len(s)), 'G': ([0] * len(s)), 'T': ([0] * len(s))}
        self.add(s)

    def add(self, dna):
        for i in range(0, len(dna)):
            self.profile[dna[i]][i] += 1

    def getConcensus(self):
        res = ''
        for i in range(0, len(self.profile['A'])):
            col = [self.profile['A'][i], self.profile['C'][i], self.profile['G'][i], self.profile['T'][i]]
            m = col.index(max(col))
            if m == 0:
                res += 'A'
            elif m == 1:
                res += 'C'
            elif m == 2:
                res += 'G'
            elif m == 3:
                res += 'T'
        return res


    def __str__(self):
        res = ''
        for i in 'ACGT':
            if len(res) > 0:
                res += '\n'
            res += i + ': '
            first = True
            for c in self.profile[i]:
                if not first:
                    res += ' '
                first = False
                res += str(c)
        return res


rnaCodon = {
    "UUU": 'F', "CUU": 'L', "AUU": 'I', "GUU": 'V',
    "UUC": 'F', "CUC": 'L', "AUC": 'I', "GUC": 'V',
    "UUA": 'L', "CUA": 'L', "AUA": 'I', "GUA": 'V',
    "UUG": 'L', "CUG": 'L', "AUG": 'M', "GUG": 'V',
    "UCU": 'S', "CCU": 'P', "ACU": 'T', "GCU": 'A',
    "UCC": 'S', "CCC": 'P', "ACC": 'T', "GCC": 'A',
    "UCA": 'S', "CCA": 'P', "ACA": 'T', "GCA": 'A',
    "UCG": 'S', "CCG": 'P', "ACG": 'T', "GCG": 'A',
    "UAU": 'Y', "CAU": 'H', "AAU": 'N', "GAU": 'D',
    "UAC": 'Y', "CAC": 'H', "AAC": 'N', "GAC": 'D',
    "UAA": '', "CAA": 'Q', "AAA": 'K', "GAA": 'E',
    "UAG": '', "CAG": 'Q', "AAG": 'K', "GAG": 'E',
    "UGU": 'C', "CGU": 'R', "AGU": 'S', "GGU": 'G',
    "UGC": 'C', "CGC": 'R', "AGC": 'S', "GGC": 'G',
    "UGA": '', "CGA": 'R', "AGA": 'R', "GGA": 'G',
    "UGG": 'W', "CGG": 'R', "AGG": 'R', "GGG": 'G'
}

reverseRNA = {}
for (p, r) in tuple(rnaCodon.items()):
    if not r in reverseRNA:
        reverseRNA[r] = []
    reverseRNA[r] += [p]


def dna2rna(dna):
    return dna.replace('T', 'U')


def rna2dna(rna):
    return rna.replace('U', 'T')


def rna2protein(rna):
    res = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        s = rnaCodon[codon]
        if len(s) == 0:
            return res
        res += s
    return res


def getFrame(rna):
    res = ''
    for i in range(0, len(rna), 3):
        codon = rna[i:i + 3]
        s = rnaCodon[codon]
        if len(s) == 0:
            return res
        res += s
    return None


monoisotopic_mass_table = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333
}

_reversed_monoisotopic_mass_table = {
    71.03711: 'A',
    103.00919: 'C',
    115.02694: 'D',
    129.04259: 'E',
    147.06841: 'F',
    57.02146: 'G',
    137.05891: 'H',
    113.08406: 'I',
    128.09496: 'K',
    #    113.08406: 'L',
    131.04049: 'M',
    114.04293: 'N',
    97.05276: 'P',
    128.05858: 'Q',
    156.10111: 'R',
    87.03203: 'S',
    101.04768: 'T',
    99.06841: 'V',
    186.07931: 'W',
    163.06333: 'Y'
}


def getIsotopicWeight(protein):
    res = 0
    for c in protein:
        res += monoisotopic_mass_table[c]
    return res


def getRoughIsotopicWeight(protein):
    res = 0
    for c in protein:
        res += int(monoisotopic_mass_table[c])
    return res


def getSymbol(weight):
    sorted_keys = sorted(_reversed_monoisotopic_mass_table.keys())
    for k in sorted_keys:
        if abs(weight - k) <= 0.0001:
            return _reversed_monoisotopic_mass_table[k]
    return None