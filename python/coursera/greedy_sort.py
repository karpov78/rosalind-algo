def print_perm(p):
    return '(' + ' '.join(['%+d' % x for x in p]) + ')'


p = raw_input()
perm = [int(x) for x in p[1:-1].split(' ')]

with open('/Users/evgeny/Downloads/result.txt', 'w') as f:
    for k in xrange(1, len(perm) + 1):
        if abs(perm[k - 1]) != k:
            for j in xrange(k, len(perm)):
                if abs(perm[j]) == k:
                    perm = perm[:k - 1] + [-x for x in reversed(perm[k - 1:j + 1])] + perm[j + 1:]
                    f.write(print_perm(perm) + '\n')
                    break
        if perm[k - 1] == -k:
            perm[k - 1] = k
            f.write(print_perm(perm) + '\n')