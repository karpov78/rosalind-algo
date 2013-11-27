if __name__ == '__main__':
    a = [float(x) for x in input().split()]
    b = []
    for p in a:
        q = 1 - p
        b.append(1 - q * q - p * p)
    print(' '.join(["%.3f" % x for x in b]))
