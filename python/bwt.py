def bwt(s):
    rotations = []
    for i in xrange(len(s)):
        rotations.append(s[i:] + s[:i])
    rotations.sort()
    return ''.join([x[-1] for x in rotations])


s = raw_input()
print bwt(s)