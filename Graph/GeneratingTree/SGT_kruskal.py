inf = float('inf')
def SGT_kruskal(graph):
    vnum = len(graph)
    rep_v = [i for i in range(vnum)]
    edges = get_sort(graph)
    lines = []
    for weight, vi, vj in edges:
        if rep_v[vi] != rep_v[vj]:
            lines.append((vi, vj, weight))
            if len(lines) == vnum - 1:
                break
            rep, orep = rep_v[vi], rep_v[vj]
            for i in range(len(rep_v)):
                if rep_v[i] == orep:
                    rep_v[i] = rep
    if len(lines) == vnum - 1:
        return lines
    else:
        return False

def get_sort(graph):
    res = []
    for i in range(len(graph)):
        ks = outline(graph, i)
        for m in range(len(ks)):
            res.append(ks[m])
    res.sort()
    return res


def outline(graph, i):
    row = graph[i]
    res = []
    for s in range(len(row)):
        if  row[s] != 0 and row[s] != inf:
            res.append((row[s], i, s))
    return res

if __name__ == '__main__':
    test = [[0, 2, 5, 7, inf, inf, inf], [2, 0, inf, 4, 12, inf, 5], \
            [5, inf, 0, 8, inf, 13, inf], [7, 4, 8, 0, inf, inf, 3],\
            [inf, 12, inf, inf, 0, inf, 7], [inf, inf, 13, inf, inf, 0, 15],\
            [inf, 5, inf, 3, 7, 15, 0]]
    k = SGT_kruskal(test)
    print(k)
