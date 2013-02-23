from python.suff import SuffixTree

def cmp(a, b):
    return (a > b) - (a < b)


def findPivot(a, i, j):
    return i


def swap(a, i, j):
    c = a[i]
    a[i] = a[j]
    a[j] = c


def partition(a, start, end, p, cmp):
    if p > start:
        swap(a, p, start)

    i = start + 1
    for j in range(start + 1, end):
        if cmp(a[start], a[j]) > 0:
            # swap
            swap(a, i, j)
            i += 1
    swap(a, start, i - 1)
    return i - 1


def quicksort(a, c=lambda x, y: x - y, i=0, j=None):
    if not j: j = len(a)
    if j - i <= 1: return 0

    ncmp = 0
    stack = [(i, j)]
    while len(stack) > 0:
        start, end = stack.pop()

        if end - start <= 1: continue

        ncmp += end - start - 1
        p = findPivot(a, start, end)
        index_p = partition(a, start, end, p, c)
        stack.append((start, index_p))
        stack.append((index_p + 1, end))
    return ncmp


def traverse(root, prefix='', result=None):
    if not result: result = {}

    if len(prefix) > 20 and len(root.edges) >= 2:
        result[prefix] = root.power()
    for e in root.edges:
        result = traverse(e.end, prefix + e.value, result)
    return result


def validate(s, curr):
    i = 0
    firstMatch = False
    while i < len(s):
        if s[i:i + len(curr)] == curr:
            if firstMatch:
                return True
            else:
                i += len(curr)
                firstMatch = True
        i += 1
    return False

if __name__ == '__main__':
    s = input()
    t = SuffixTree(s + '$')
    mrep = traverse(t.root)
    keys = list(mrep.keys())
    quicksort(keys, c=lambda x, y: mrep[y] - mrep[x] if mrep[x] != mrep[y] else cmp(x[::-1], y[::-1]))
    i = 1
    while i < len(keys):
        curr = keys[i]
        prev = keys[i - 1]

        if not validate(s, curr):
            del keys[i]
            continue

        if curr[1:] == prev and mrep[curr] == mrep[prev]:
            del keys[i - 1]
        else:
            i += 1
        #print('\n'.join(['%s -> %d' % (x, mrep[x]) for x in keys]))
    print('\n'.join(keys))
