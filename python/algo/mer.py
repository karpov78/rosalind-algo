def merge(a, b):
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1
    return res

if __name__ == '__main__':
    with open('/Users/evgeny/Downloads/rosalind_mer.txt') as f:
        n = int(f.readline())
        a = [int(x) for x in f.readline().split()]
        m = int(f.readline())
        b = [int(x) for x in f.readline().split()]
    print ' '.join([str(x) for x in merge(a, b)])