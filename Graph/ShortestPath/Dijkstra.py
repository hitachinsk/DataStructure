inf = float('inf')
def dijkstra(graph, v):
    vnum = len(graph)
    cdis = [inf] * vnum
    visited = [0] * vnum
    cdis[v] = 0
    node = v
    while visited != [1] * vnum:
        visited[node] = 1
        temp = outline(graph, node)
        if temp == None:
            node = v
            temp = outline(graph, node)
        for w, out, index in temp:
            if visited[index] == 0:
                if cdis[index] > cdis[out] + w:
                    cdis[index] = cdis[out] + w
        min_d = inf
        for i in range(len(visited)):
            if visited[i] == 0:
                if cdis[i] < min_d:
                    min_d = cdis[i]
                    node = i
        if min_d == inf:
            break
    return cdis

def outline(graph, v):
    row = graph[v]
    res = []
    for i in range(len(row)):
        if row[i] != 0 and row[i] != inf:
            res.append((row[i], v, i))
    return res

#Dijkstra for all nodes
def dijkstra_all(graph):
    vnum = len(graph)
    for i in range(vnum):
        res = dijkstra(graph, i)
        print(res)


if __name__ == '__main__':
    test = [[0, inf, 5, 2, inf, inf, inf], [11, 0, 4, inf, inf, 4, inf],\
            [inf, 3, 0, inf, 2, 7, inf], [inf, inf, inf, 0, inf, inf, inf],\
            [inf, inf, inf, inf, 0, inf, 2], [inf, inf, inf, inf, inf, 0, 3],\
            [inf, inf, inf, inf, inf, inf, 0]]
    dijkstra_all(test)
