__author__ = 'evgeny'

factorial_cache = {}


def fact(x):
    if x in factorial_cache:
        return factorial_cache[x]
    if x == 1:
        return 1
    f = x * fact(x - 1)
    factorial_cache[x] = f
    return f


if __name__ == '__main__':
    s = raw_input()

    a_num = 0
    c_num = 0

    for c in s:
        if c == 'A':
            a_num += 1
        elif c == 'C':
            c_num += 1

    print fact(a_num) * fact(c_num)