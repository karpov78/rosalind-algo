from util import test_data


def merge_sort(_a, left=0, right=-1):
    if right == -1:
        right = len(_a)
    if left >= right - 1:
        return a[left:right], 0
    mid = (left + right) // 2
    l, l_i = merge_sort(_a, left, mid)
    r, r_i = merge_sort(_a, mid, right)
    m, m_i = merge(l, r)
    return m, l_i + r_i + m_i


def merge(_a, _b):
    _res = []
    _i = 0
    _j = 0
    _inv = 0
    while _i < len(_a) and _j < len(_b):
        if _a[_i] <= _b[_j]:
            _res.append(_a[_i])
            _i += 1
        else:
            _res.append(_b[_j])
            _j += 1
            _inv += len(_a) - _i
    while _i < len(_a):
        _res.append(_a[_i])
        _i += 1
    while _j < len(_b):
        _res.append(_b[_j])
        _j += 1
    return _res, _inv

if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        n = int(f.readline())
        a = [int(x) for x in f.readline().split()]

    sa, inv = merge_sort(a)
    print inv