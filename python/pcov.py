def build_deBruijin_graph(s):
    return {r[:-1]: r[1:] for r in s}


s = []
while True:
    l = input()
    if not l: break
    s.append(l)

edges = build_deBruijin_graph(s)

start_node = s[0][:-1]
visited_nodes = {start_node}
string = start_node

node = edges[start_node]
while not node in visited_nodes:
    visited_nodes.add(node)
    string += node[-1]
    node = edges[node]

i = 0
max = 0
while i < (len(string) / 2):
    if string[:i] == string[-i:]:
        max = i
    i += 1
print(string[:-max])
