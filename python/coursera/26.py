def Pr(s, profile):
    res = 1
    for i in range(len(s)):
        res *= profile[i][s[i]]
    return res


s = raw_input()
k = int(raw_input())
profile = []
raw_input()
for i in range(k):
    row = [float(x) for x in raw_input().split(' ')]
    profile.append({'A': row[0], 'C': row[1], 'G': row[2], 'T': row[3]})

res = (0, '')
for i in range(len(s) - k + 1):
    kmer = s[i: i + k]
    pr = Pr(kmer, profile)
    if pr > res[0]:
        res = (pr, kmer)
print res[1]