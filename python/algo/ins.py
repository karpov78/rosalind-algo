def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def ins_sort_swaps(a):
    res = 0
    for i in xrange(1, len(a)):
        k = i
        while k > 0 and a[k] < a[k - 1]:
            swap(a, k - 1, k)
            res += 1
            k -= 1
    return res


if __name__ == '__main__':
    with open('/Users/evgeny/Downloads/rosalind_ins.txt') as f:
        n = int(f.readline())
        a = [int(x) for x in f.readline().split()]
    print ins_sort_swaps(a)