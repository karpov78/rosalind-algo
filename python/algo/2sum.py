from util import test_data


def find_2sum(_a):
    items = dict()
    for i in xrange(len(_a)):
        if -_a[i] in items:
            return '%d %d' % (items[-_a[i]] + 1, i + 1)
        else:
            items[_a[i]] = i
    return -1

if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        k, n = (int(x) for x in f.readline().split())
        for i in xrange(k):
            arr = [int(x) for x in f.readline().split()]
            print find_2sum(arr)