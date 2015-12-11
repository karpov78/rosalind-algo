from util import test_data, read_ugraph_to_list


def degree(g, u):
    res = [0] * u
    for n1, n2 in g:
        res[n1 - 1] += 1
        res[n2 - 1] += 1
    return res


if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        u, g = read_ugraph_to_list(f)
    result = degree(g, u)
    print ' '.join([str(x) for x in result])