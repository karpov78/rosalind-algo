def mDiff(s1, s2, diff=None):
    if not diff: diff = {}
    for i1 in s1:
        for i2 in s2:
            d = round(i1 - i2, 6)
            if d in diff:
                diff[d] += 1
            else:
                diff[d] = 1
    return diff


def getMaxMultiplicity(diff):
    max = 0
    max_key = None
    for (k, v) in diff.items():
        if v > max:
            max = v
            max_key = k
    return max, max_key

if __name__ == '__main__':
    s1 = [float(x) for x in input().split(' ')]
    s2 = [float(x) for x in input().split(' ')]

    spectral_conv = mDiff(s1, s2)
    max, max_key = getMaxMultiplicity(spectral_conv)
    print(max)
    print(max_key)