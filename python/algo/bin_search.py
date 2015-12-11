def search(a, x):
    start = 0
    end = len(a) - 1
    while start < end:
        mid = (start + end) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    if start == end and a[start] == x:
        return start
    return -1

if __name__ == '__main__':
    with open('/Users/evgeny/Downloads/rosalind_bins.txt') as f:
        n = int(f.readline())
        m = int(f.readline())
        a = [int(x) for x in f.readline().split()]
        b = [int(x) for x in f.readline().split()]

        res = []
        for i in b:
            index = search(a, i)
            if index >= 0:
                res.append(index + 1) # 1-based index
            else:
                res.append(index)
        print ' '.join([str(i) for i in res])