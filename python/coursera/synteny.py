def reverseComplement(dna):
    lookup = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([lookup[c] for c in reversed(dna)])


k = int(raw_input())
s = raw_input()
t = raw_input()
# with open('/Users/evgeny/Downloads/shared_kmer.txt', 'r') as f:
#     f.readline()
#     k = int(f.readline().strip())
#     s = f.readline().strip()
#     t = f.readline().strip()
#     f.readline()
#     expected = set()
#     while True:
#         l = f.readline()
#         if not l:
#             break
#         expected.add(l.strip())

t_dict = dict()
for j in xrange(len(t) - k + 1):
    t_ = t[j:j + k]
    if t_ in t_dict:
        t_dict[t_].append(j)
    else:
        t_dict[t_] = [j]

res = set()
for i in xrange(len(s) - k + 1):
    s_ = s[i:i + k]
    if s_ in t_dict:
        for j in t_dict[s_]:
            res.add("(%d, %d)" % (i, j))
    rs_ = reverseComplement(s_)
    if rs_ in t_dict:
        for j in t_dict[rs_]:
            res.add("(%d, %d)" % (i, j))
print '\n'.join(res)
# assert res == expected, "Expected: %s\n, but was: %s" % (str(expected), str(res))