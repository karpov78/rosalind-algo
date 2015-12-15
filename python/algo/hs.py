from util import test_data
from hea import MaxHeap

def heap_sort(_a):
    _res = []
    _h = MaxHeap(len(_a))
    for _x in _a:
        _h += _x
    while len(_h) > 0:
        _h.extract_max()
    return _h.items()

if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        n = int(f.readline())
        arr = [int(x) for x in f.readline().split()]
    s = heap_sort(arr)
    ss = sorted(arr)
    if s != ss:
        for i in xrange(len(s)):
            if s[i] != ss[i]:
                print "Diff at %dth position - expected %d, but was %d" % (i, ss[i], s[i])
                print ' '.join([str(x) for x in s])
                print ' '.join([str(x) for x in ss])
                break
    else:
        print ' '.join([str(x) for x in heap_sort(arr)])