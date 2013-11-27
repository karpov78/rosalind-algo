import math


def profile(motifs):
    profile = []
    for j in range(len(motifs[0])):
        p = {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}
        for s in motifs:
            p[s[j]] += 1
        p['A'] /= len(motifs)
        p['C'] /= len(motifs)
        p['G'] /= len(motifs)
        p['T'] /= len(motifs)
        profile.append(p)
    return profile


def Pr(s, profile):
    res = 1
    for i in range(len(s)):
        res *= profile[i][s[i]]
    return res


def MostProbable(profile, k, s):
    res = (Pr(s[:k], profile), s[:k])
    for i in range(1, len(s) - k + 1):
        kmer = s[i: i + k]
        pr = Pr(kmer, profile)
        if pr > res[0]:
            res = (pr, kmer)
    return res[1]


def Score(motifs):
    size = len(motifs)
    entropy = 0
    for j in range(len(motifs[0])):
        m = {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}
        for i in range(size):
            m[motifs[i][j]] += 1
        e = 0
        for v in m.values():
            p = v / size
            e += 0 if p == 0 else p * math.log(p, 2)
        entropy += -e
    return entropy


def GreedyMotifSearch(dna, k):
    bestMotifs = []
    for s in dna:
        bestMotifs.append(s[:k])
    bestScore = Score(bestMotifs)

    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i: i + k]]
        for t in range(1, len(dna)):
            pr = profile(motifs)
            motifs.append(MostProbable(pr, k, dna[t]))
        s = Score(motifs)
        if s < bestScore:
            bestMotifs = motifs
            bestScore = s
    return bestMotifs


k, t = (int(x) for x in raw_input().split(' '))
dna = []
for i in range(t):
    dna.append(raw_input().strip())

m = GreedyMotifSearch(dna, k)
print '\n'.join(m)

test = "AGTGGGTATCTC TAAAAAGGTATA AACCACGAGTAC TGTCATGTGCGG AACCTAAACCCT AGTCGTTATCCC AGTAATATGTAC AGTGGTTATCAC AGTGGTTATCCC AGTGGCTATCGC AGTGGATATCCC AGTGAGAAGCAA AGTGACTAGACA TAAGACTAGTTA TATGAAGGGTGA AGTCGGGATAAC AGTGGGTATCTC AGCGGTTAGTCA AGTGAAATTCCT TGTGGATGGCTT TGTAGGTATCAC TGCAGATATCCA TGTGGTTATCAC TGTCATTATTCA TGCGTAGATCAA".split(
    ' ')
if test != m:
    print "Error"