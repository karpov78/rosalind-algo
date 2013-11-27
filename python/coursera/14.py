from timer import Timer
import math


def getNumOfProteins(n):
    global weights
    known_masses = {0: 1}
    res = 0
    while len(known_masses) > 0:
        new_masses = {}
        for c in known_masses.keys():
            for w in weights:
                new_w = c + w
                c_count = known_masses[c]
                if new_w == n:
                    res += c_count
                elif new_w < n:
                    if new_w in new_masses:
                        new_masses[new_w] += c_count
                    else:
                        new_masses[new_w] = c_count
                else:
                    break
        known_masses = new_masses
    return res


mass_table = {'A': 71, 'C': 103, 'D': 115, 'E': 129, 'F': 147, 'G': 57, 'H': 137, 'I': 113, 'K': 128, 'M': 131,
              'N': 114, 'P': 97, 'R': 156, 'S': 87, 'T': 101, 'V': 99, 'W': 186, 'Y': 163}

weights = sorted(mass_table.values())

with Timer() as t:
    x2 = None
    c1 = 0
    c2 = 0
    for x in range(6000, 10000):
        x1 = getNumOfProteins(x) if not x2 else x2
        x2 = getNumOfProteins(x + 1)

        c1 = c2
        c2 = float(x2) / x1
        if c1 > 0:
            if c2 - c1 < 0.000002:
                print c2
                break
print t