known_distances = {}

def flip(s, i, j):
    while i < j:
        c = s[i]
        s[i] = s[j]
        s[j] = c
        i += 1
        j -= 1

def cmp(c1, c2, t):
    return t.index(c2) - t.index(c1)

def b(s, t):
    b = []
    direction = 0
    strike_start = -1
    for i in range(len(s)):
        if strike_start == -1:
            strike_start = i
            continue

        r = cmp(s[i - 1], s[i], t)
        if r == direction:
            continue
        if direction == 0 and abs(r) == 1:
            direction = r
        else:
            b.append((strike_start, i - 1, direction))
            strike_start = i
            direction = r if abs(r) == 0 else 0
    b.append((strike_start, len(s) - 1, direction))
    return b


def flip_strikes(break_pts, s, t, direction):
    falling_strikes = [x for x in break_pts if x[2] == direction]
    falling_strikes.sort(key=lambda x: x[0] - x[1])
    for i in falling_strikes:
        print("Trying %s" % str(i))
        flip(s, i[0], i[1])
        new_breaks = b(s, t)
        print("\told: %d new: %d" % (len(break_pts), len(new_breaks)))
        if len(new_breaks) < len(break_pts):
            print("\tapply")
            return True
        flip(s, i[0], i[1])
    return False

def distance(s, t):
    key = ' '.join(s) + ' '.join(t)
    if key in known_distances:
        return known_distances[key]

    break_pts = b(s, t)

    if len(break_pts) == 1:
        result = [] if break_pts[0][2] == 1 else [(1, len(s))]
        known_distances[key] = result
        return result

    result = [None] * (len(s) + 1)
    result_len = len(s) + 1
    for i in range(len(s)):
        for j in range(i, len(s)):
            flip(s, i, j)
            brk = b(s, t)
            if len(brk) < len(break_pts):
                d = distance(s, t)
                if len(d) < result_len:
                    result = [(i + 1, j + 1)] + d
                    result_len = len(d)
            flip(s, i, j)

    known_distances[key] = result
    return result


s = input().split(' ')
t = input().split(' ')
dist = distance(s, t)
print(len(dist))
print('\n'.join([' '.join([str(y) for y in x]) for x in dist]))
