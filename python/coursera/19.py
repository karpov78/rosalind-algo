def convolution(s):
    res = {}
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            d = abs(s[i] - s[j])

            if d == 0: continue

            if d in res:
                res[d] += 1
            else:
                res[d] = 1

    ret = []
    for d, c in sorted(res.items(), key=lambda k: -k[1]):
        for i in range(c):
            ret.append(d)
    return ret


spectrum = [int(x) for x in raw_input().split(' ')]
print ' '.join([str(x) for x in convolution(spectrum)])


# with open('/Users/evgeny/Downloads/spectral_convolution_data.txt', 'r') as f:
#     f.readline()
#     spectrum = [int(x) for x in f.readline().split(' ')]
#     f.readline()
#     expected = [int(x) for x in f.readline().split(' ')]
#
#     c = convolution(spectrum)
#     if c != expected:
#         print "Fail!"