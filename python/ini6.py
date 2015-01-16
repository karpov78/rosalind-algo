if __name__ == '__main__':
    s = raw_input().split(' ')
    d = {}
    for w in s:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1

    print '\n'.join(x + ' ' + str(y) for x, y in d.items())