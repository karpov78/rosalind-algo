from util import test_data
from mer import merge

def merge_sort(_a, left=0, right=-1):
    if right == -1:
        right = len(_a)
    if left >= right - 1:
        return a[left:right]
    mid = (left + right) // 2
    l = merge_sort(_a, left, mid)
    r = merge_sort(_a, mid, right)
    return merge(l, r)

if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        n = int(f.readline())
        a = [int(x) for x in f.readline().split()]
    print ' '.join([str(x) for x in merge_sort(a)])