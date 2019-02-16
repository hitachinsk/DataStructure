inf = float('inf')
def toposort(graph):
    vnum = len(graph)
    index = get_index(graph)
    zerov = -1
    toposeq = []
    for vi in range(vnum):
        if index[vi] == 0:
            index[vi] = zerov
            zerov = vi
    for n in range(vnum):
        if zerov == -1:
            break
        vi = zerov
        zerov = index[zerov]
        toposeq.append(vi)
        for out, indgree in outline(graph[vi], vi):
            index[indgree] -= 1
            if index[indgree] == 0:
                index[indgree] = zerov
                zerov = indgree
        
    if len(toposeq) == vnum:
        return toposeq
    else:
        return False

def get_index(graph):
    res = [0] * len(graph)
    k = []
    for i in range(len(graph)):
        k.append(outline(graph[i], i))
    for i in range(len(k)):
        for each in k[i]:
            res[each[1]] += 1
    return res

def outline(line, num):
    res = []
    for j in range(len(line)):
        if line[j] != 0 and line[j] != inf:
            res.append((num, j))
    return res

if __name__ == '__main__':
    test = [[0, 1, 1, 1, inf, inf, inf], [inf, 0, inf, inf, 1, inf, inf],\
            [inf, inf, 0, inf, inf, 1, inf], [inf, inf, inf, 0, inf, 1, inf],\
            [inf, inf, inf, inf, 0, inf, 1], [inf, inf, inf, inf, inf, 0, 1],\
            [inf, inf, inf, inf, inf, inf, 0]]
    s = toposort(test)
    print(s)
