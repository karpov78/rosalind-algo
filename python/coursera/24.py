from util import getHammingDistance


def enumPatterns(p, score, maxScore, idx=0):
    k = len(p)
    if idx < k:
        s = (maxScore, p)
        for c in 'ACGT':
            p[idx] = c
            m = enumPatterns(p, score, maxScore, idx + 1)
            if m[0] < s[0]:
                s = m
        return s
    else:
        return score(p), ''.join(p)


def d(p, dna):
    res = 0
    for s in dna:
        res += d_row(p, s)
    return res


def d_row(p, s):
    k = len(p)
    minScore = k
    for i in range(len(s) - k + 1):
        match = s[i:i + k]
        d = getHammingDistance(p, match)
        if d < minScore:
            minScore = d
        if minScore == 0:
            break
    return minScore


def MedianString(dna, k):
    return enumPatterns(['A'] * k, lambda p: d(p, dna), k * len(dna))


if __name__ == '__main__':
    k = int(raw_input())
    dna = []
    while True:
        s = raw_input()
        if not s:
            break
        dna.append(s)

    print MedianString(dna, k)[1]
