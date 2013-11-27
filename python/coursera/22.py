import util


def dContains(s, p, d):
    k = len(p)
    for i in range(len(s) - k + 1):
        if util.getHammingDistance(s[i:i + k], p) <= d:
            return True
    return False


def MotifEnumeration(dna, k, d):
    found = set()
    for seq in dna:
        for i in range(len(seq) - k):
            kmer = seq[i:i + k]
            dc_kmer = util.dClosure([x for x in kmer], d)
            for ds in dc_kmer:
                if ds in found:
                    continue
                hit = True
                for s in dna:
                    if not dContains(s, ds, d):
                        hit = False
                        break
                if hit:
                    found.add(ds)
    return found


k, d = (int(x) for x in raw_input().split(" "))
dna = []
while True:
    s = raw_input()
    if not s:
        break
    dna.append(s)
motifs = MotifEnumeration(dna, k, d)
print ' '.join(sorted(motifs))