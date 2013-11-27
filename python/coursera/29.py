import util
import random


def MostProbable(profile, dna, k):
    res = (util.ProfileProbability(dna[:k], profile), dna[:k])
    for i in range(1, len(dna) - k + 1):
        kmer = dna[i: i + k]
        pr = util.ProfileProbability(kmer, profile)
        if pr > res[0]:
            res = (pr, kmer)
    return res[1]


def Motifs(profile, dna, k):
    motifs = []
    for s in dna:
        motifs.append(MostProbable(profile, s, k))
    return motifs


def RandomMotif(k, alphabet=['A', 'C', 'G', 'T']):
    random.seed()
    s = ''
    for i in xrange(k):
        s += random.choice(alphabet)
    return s


def UnpopularScore(motifs):
    size = len(motifs)
    res = 0
    for j in range(len(motifs[0])):
        m = {'A': 0.0, 'C': 0.0, 'G': 0.0, 'T': 0.0}
        for i in range(size):
            m[motifs[i][j]] += 1
        s = 0
        best = 0
        for v in m.values():
            if v > best:
                s += best
                best = v
            else:
                s += v
        res += s
    return res


def RandomizedMotifSearch(dna, k):
    bestMotifs = []
    for s in range(len(dna)):
        bestMotifs.append(RandomMotif(k))
    bestScore = UnpopularScore(bestMotifs)
    motifs = list(bestMotifs)

    while True:
        profile = util.PseudocountsProfile(motifs)
        motifs = Motifs(profile, dna, k)
        s = UnpopularScore(motifs)
        if s < bestScore:
            bestMotifs = motifs
            bestScore = s
        else:
            return bestScore, bestMotifs


k, t = (int(x) for x in raw_input().split(' '))
dna = []
for i in range(t):
    dna.append(raw_input().strip())

bestScore, bestMotif = RandomizedMotifSearch(dna, k)
for i in xrange(1000):
    s, m = RandomizedMotifSearch(dna, k)
    if s < bestScore:
        bestScore = s
        bestMotif = m
print bestScore
print '\n'.join(bestMotif)

# expected = ['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']
# expectedScore = UnpopularScore(expected)
# print expectedScore