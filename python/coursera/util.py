import math
import random


def convolution(s):
    res = {}
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            d = abs(s[i] - s[j])

            if d < 57 or d >= 200:
                continue

            if d in res:
                res[d] += 1
            else:
                res[d] = 1
    return res


def expandList(l, alphabet):
    res = []
    for c in alphabet:
        res += [x + [c] for x in l]
    return res


def allKmers(s, k):
    len_s = len(s)
    if k == 0:
        return ['']
    elif k == len_s:
        return [s]
    res = []
    for i in range(len_s):
        res.append(s[i:i + min(k, len_s - i)] + s[0:max(0, i + k - len_s)])
    return res


def linearSpectrum(s):
    len_s = len(s)
    res = [0]
    for i in range(len_s):
        for j in range(i + 1, len_s + 1):
            res.append(sum(s[i:j]))
    return sorted(res)


def cyclicSpectrum(s):
    res = []
    len_s = len(s)
    for i in range(len_s + 1):
        ss = allKmers(s, i)
        for w in ss:
            res.append(sum(w))
    return sorted(res)


def Score(ps, s):
    i = 0
    j = 0
    res = 0
    while i < len(s) and j < len(ps):
        if ps[j] == s[i]:
            res += 1
            i += 1
            j += 1
        elif ps[j] < s[i]:
            j += 1
        else:
            i += 1
    return res


def dClosure(s, d, fixed=None, res=None):
    fixed = [] if not fixed else fixed
    res = set() if not res else res

    res.add(''.join(s))
    if d == 0:
        return

    for i in range(len(s)):
        if not i in fixed:
            orig = s[i]
            for ch in 'ACGT':
                if ch != orig:
                    s[i] = ch
                    dClosure(s, d - 1, fixed + [i], res)
            s[i] = orig
    return res


def getHammingDistance(s, t):
    d = 0
    for i in range(0, len(s)):
        if s[i] != t[i]:
            d += 1
    return d


def readDNA():
    dna = ''
    while True:
        line = raw_input()
        if not line:
            return dna
        dna += line.strip()


def EnthropyScore(motifs):
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


def Profile(motifs):
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


def PseudocountsProfile(motifs, skip={}):
    profile = []
    t = len(motifs)
    size = t + 1 - len(skip)
    for j in range(len(motifs[0])):
        p = {'A': 1.0, 'C': 1.0, 'G': 1.0, 'T': 1.0}
        for i in xrange(t):
            if not i in skip:
                p[motifs[i][j]] += 1
        p['A'] /= size
        p['C'] /= size
        p['G'] /= size
        p['T'] /= size
        profile.append(p)
    return profile


def ProfileProbability(s, profile):
    res = 1
    for i in range(len(s)):
        res *= profile[i][s[i]]
    return res


def Random(p):
    t = sum(p)
    f = random.random() * t
    s = 0.0
    for i in range(len(p)):
        if f < s + p[i]:
            return i
        else:
            s += p[i]
    return len(p) - 1


def MostProbable(profile, dna, k):
    res = (ProfileProbability(dna[:k], profile), dna[:k])
    for i in range(1, len(dna) - k + 1):
        kmer = dna[i: i + k]
        pr = ProfileProbability(kmer, profile)
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
        m = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
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


