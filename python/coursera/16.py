mass_table = {'A': 71, 'C': 103, 'D': 115, 'E': 129, 'F': 147, 'G': 57, 'H': 137, 'I': 113, 'K': 128, 'M': 131,
              'N': 114, 'P': 97, 'R': 156, 'S': 87, 'T': 101, 'V': 99, 'W': 186, 'Y': 163}


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


def getSpectrum(s):
    spectrum = []
    len_s = len(s)
    for i in range(len_s + 1):
        ss = allKmers(s, i)
        for w in ss:
            spectrum.append(sum(w))
    return sorted(spectrum)


def getLinearSpectrum(s):
    len_s = len(s)
    spectrum = [0]
    for i in range(len_s):
        for j in range(i + 1, len_s + 1):
            spectrum.append(sum(s[i:j]))
    return sorted(spectrum)


def pConsistent(ps, s):
    len_s = len(s)
    i = 0
    for x in ps:
        while i < len_s and x > s[i]:
            i += 1
        if i == len(s) or x != s[i]:
            return False
        i += 1
    return True


def expandList(l, s):
    res = []
    for c in mass_table.values():
        if c in s:
            res += [x + [c] for x in l]
    return res


spectrum = [int(x) for x in raw_input().split(' ')]

output = []
l = [[]]
while len(l) > 0:
    l = expandList(l, spectrum)
    new_list = []
    for p in l:
        ps = getSpectrum(p)
        pls = getLinearSpectrum(p)
        if ps == spectrum:
            output.append('-'.join([str(x) for x in p]))
        elif pConsistent(pls, spectrum):
            new_list.append(p)
    l = new_list
print ' '.join(output)