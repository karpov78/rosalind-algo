from util import test_data, swap

def par3(_a, _pivot = 0):
    _last = len(_a) - 1
    _i = 1
    _q = -1
    while _i <= _last:
        if _a[_i] == _a[_i - 1]:
            if _q == -1:
                _q = _i - 1
            _i += 1
        elif _a[_i] < _a[_i - 1]:
            if _q == -1:
                swap(_a, _i - 1, _i)
            else:
                swap(_a, _q, _i)
                _q += 1
            _i += 1
        elif _i != _last:
            swap(_a, _i, _last)
            _last -= 1
        else:
            break



if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        n = int(f.readline())
        a = [int(x) for x in f.readline().split()]

    par3(a)
    print ' '.join([str(x) for x in a])