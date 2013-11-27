def remove(s, x, start=0, end=None):
    if not end: end = len(s) - 1

    if end - start <= 1:
        if s[start] == x:
            del s[start]
        elif s[end] == x:
            del s[end]
        else:
            return False
        return True

    mid = int((end + start) / 2)
    if s[mid] == x:
        del s[mid]
        return True
    elif s[mid] > x:
        return remove(s, x, start, mid)
    else:
        return remove(s, x, mid, end)


failed_n = set()


def tryN(s, items, n):
    for c in items:
        if not remove(s, abs(c - n)):
            return None

    items.add(n)

    if len(s) == 0:
        return items

    for c in items:
        result = tryN(list(s), items, abs(s[-1] - c))
        if result: return result

    items.remove(n)
    return None


def recreateSet(s):
    s.sort()
    result = {0, s[-1]} # set minimum element to 0
    del s[-1]

    for c in result:
        ret = tryN(list(s), result, abs(s[-1] - c))
        if ret: return ret

    return None


if __name__ == '__main__':
    s = [int(x) for x in input().split(' ')]
    print(' '.join([str(x) for x in sorted(recreateSet(s))]))
