from python.suff_tree import SuffixTree


def m(n):
    result = [0] * n
    x = n
    y = 1
    for i in range(n):
        if y > x - i:
            result[i] = x - i
        else:
            y *= 4
            result[i] = min(y, x - i)
    return result


def calculate_subs(s_tree):
    result = 0
    nodes = [s_tree.root]
    while len(nodes) > 0:
        node = nodes.pop()
        for e in node.edges:
            result += e.length
            nodes.append(e.end)
    return result


if __name__ == '__main__':
    s = input()
    print("Building suffix tree...")
    s_tree = SuffixTree(s, progress=True)
    s_len = len(s)
    print("Calculating subs...")
    sub_total = calculate_subs(s_tree)
    print("Calculating m...")
    m_arr = m(s_len)
    m_total = sum(m_arr)
    print(sub_total)
    print(m_total)
    print(sub_total / m_total)

