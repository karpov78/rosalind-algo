from util import test_data


def find_3sum(_a):
    sum1 = {}
    sum2 = {}
    for _idx in xrange(len(_a)):
        if -1 * _a[_idx] in sum2:
            s2 = sum2[-1 * _a[_idx]]
            return (s2[0] + 1, s2[1] + 1, _idx + 1)
        for v, j in sum1.items():
            if _a[_idx] + v not in sum2:
                sum2[_a[_idx] + v] = (j, _idx)
        if _a[_idx] not in sum1:
            sum1[_a[_idx]] = _idx
    return None


if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        k, n = (int(x) for x in f.readline().split())
        res = []
        for i in xrange(k):
            a = [int(x) for x in f.readline().split()]
            res.append(find_3sum(a))
    print '\n'.join(['-1' if not s else ' '.join([str(x) for x in s]) for s in res])