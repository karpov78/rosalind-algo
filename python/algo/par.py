from util import test_data, swap

def par(_a, _pivot = 0):
    last = len(_a) - 1
    i = 1
    while i <= last:
        if _a[i] <= a[i - 1]:
            swap(_a, i - 1, i)
            i += 1
        elif i != last:
            swap(_a, i, last)
            last -= 1
        else:
            break



if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        n = int(f.readline())
        a = [int(x) for x in f.readline().split()]

    par(a)
    print ' '.join([str(x) for x in a])