import util
import random


def ProfileRandomlyGeneratedString(profile, s, k):
    p = []
    for i in xrange(len(s) - k + 1):
        p.append(util.ProfileProbability(s[i: i + k], profile))
    o = util.Random(p)
    return s[o: o + k]


def GibbsSampler(dna, k, N):
    t = len(dna)
    len_s = len(dna[0])
    bestMotifs = []
    for s in dna:
        i = random.randint(0, len_s - k)
        bestMotifs.append(s[i: i + k])
    bestScore = util.UnpopularScore(bestMotifs)
    motifs = list(bestMotifs)

    for i in xrange(N):
        x = random.randint(0, t - 1)
        profile = util.PseudocountsProfile(motifs, {x})
        motifs[x] = ProfileRandomlyGeneratedString(profile, dna[x], k)
        s = util.UnpopularScore(motifs)
        if s < bestScore:
            bestMotifs = list(motifs)
            bestScore = s
    return bestScore, bestMotifs


k, t, N = (int(x) for x in raw_input().split(' '))
dna = []
for i in range(t):
    dna.append(raw_input().strip())

bestScore, bestMotif = GibbsSampler(dna, k, N)
for i in xrange(19):
    random.seed()
    s, m = GibbsSampler(dna, k, N)
    if s < bestScore:
        bestScore = s
        bestMotif = m
print bestScore
print '\n'.join(bestMotif)

expected = ['TCTCGGGG', 'CCAAGGTG', 'TACAGGCG', 'TTCAGGTG', 'TCCACGTG']
expectedScore = util.UnpopularScore(expected)
print expectedScore