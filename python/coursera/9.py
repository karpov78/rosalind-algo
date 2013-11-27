from util import reverseRNA

if __name__ == '__main__':
    s = raw_input()
    r = 1
    for c in s:
        r *= len(reverseRNA[c])
    print r