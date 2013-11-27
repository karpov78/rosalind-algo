from util import getRoughIsotopicWeight


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
            spectrum.append(getRoughIsotopicWeight(w))
    return sorted(spectrum)


if __name__ == '__main__':
    s = raw_input()
    print ' '.join(['%d' % x for x in getSpectrum(s)])