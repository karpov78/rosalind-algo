from collections import defaultdict


def sort_bucket(str, bucket, order):
    d = defaultdict(list)
    for i in bucket:
        key = str[i:i + order]
        d[key].append(i)
    result = []
    for k, v in sorted(d.iteritems()):
        if len(v) > 1:
            result += sort_bucket(str, v, order * 2)
        else:
            result.append(v[0])
    return result


def suffix_array_ManberMyers(str):
    return sort_bucket(str, (i for i in xrange(len(str))), 1)


if __name__ == "__main__":
    s = raw_input()
    print len(s)
    with open('/Users/evgeny/Downloads/result.txt', 'w') as f:
        f.write(', '.join([str(x) for x in suffix_array_ManberMyers(s)]))
