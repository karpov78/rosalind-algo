from collections import defaultdict


def sort_bucket(str, bucket, order, k, index=0):
    d = defaultdict(list)
    for i in bucket:
        key = str[i:i + order]
        d[key].append(i)
    result = []
    for key, v in sorted(d.iteritems()):
        if len(v) > 1:
            l, i = sort_bucket(str, v, order * 2, k, index)
            result += l
            index = i
        else:
            if v[0] % k == 0:
                result.append((index, v[0]))
            index += 1
    return result, index


def suffix_array_ManberMyers(str, k):
    return sort_bucket(str, (i for i in xrange(len(str))), 1, k)[0]


if __name__ == '__main__':
    s = raw_input()
    k = int(raw_input())
    # with open('/Users/evgeny/Downloads/partialSuffixArray.txt', 'r') as f:
#     f.readline()
#     s = f.readline().strip()
#     k = int(f.readline().strip())
#     f.readline()
#     exp = []
#     while True:
#         l = f.readline()
#         if not l: break
#         exp.append(l.strip())

    sa = suffix_array_ManberMyers(s, k)
    res = []
    for suff in sa:
        res.append('%d,%d' % suff)
    print '\n'.join(res)
#   assert exp == res

