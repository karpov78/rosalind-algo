import os.path


def test_data(module):
    name = os.path.splitext(os.path.basename(module))[0]
    return '/Users/evgeny/Downloads/rosalind_%s.txt' % name


def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t