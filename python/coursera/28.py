import util


def MostProbable(profile, k, s):
    res = (util.ProfileProbability(s[:k], profile), s[:k])
    for i in range(1, len(s) - k + 1):
        kmer = s[i: i + k]
        pr = util.ProfileProbability(kmer, profile)
        if pr > res[0]:
            res = (pr, kmer)
    return res[1]


def GreedyMotifSearch(dna, k):
    bestMotifs = []
    for s in dna:
        bestMotifs.append(s[:k])
    bestScore = util.EnthropyScore(bestMotifs)

    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i: i + k]]
        for t in range(1, len(dna)):
            pr = util.PseudocountsProfile(motifs)
            motifs.append(MostProbable(pr, k, dna[t]))
        s = util.EnthropyScore(motifs)
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

test = "CATCGCTTAACT CCTCACTGAACT CGTCACTACACT CTTCTCTCGACT CTTCACTCCACT CCTCGCTAAACT CTTCACTCCACT CTTCGCTAGACT CTTCACTGAACT CGTCCCTGGACT CCTCGCTGAACT CTTCACTTAACT CGTCACTTAACT CATCTCTTTACT CGTCGCTGGACT CTTCTCTGCACT CCTCTCTGCACT CGTCTCTAGACT CATCACTTCACT CATCGCTCAACT CATCACTAGACT CATCACTCGACT CGTCCCTACACT CTTCGCTTGACT CTTCCCTGAACT".split(
    ' ')
if test != m:
    print "Error"