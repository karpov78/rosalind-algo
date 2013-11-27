if __name__ == '__main__':
    data = []
    while True:
        s = input()
        if not s: break
        data.append(s)

    data.sort(key=lambda x: -len(x))
    total = 0
    for c in data:
        total += len(c)

    n50 = 0
    fixN50 = True
    n75 = 0
    s = 0
    for c in data:
        s += len(c)
        ratio = s / total
        if ratio < 0.5:
            n75 = len(c)
            n50 = n75
        elif ratio < 0.75:
            if fixN50:
                fixN50 = False
                n50 = len(c)
            n75 = len(c)
        else:
            n75 = len(c)
            break
    print('%d %d' % (n50, n75))
