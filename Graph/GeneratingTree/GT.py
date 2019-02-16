#递归方式求得一个图的生成树
inf = float('inf')
def graph_outedges(graph, v):
    if 0 > v or v > len(graph):
        raise ValueError('The node is illegal')
    row = graph[v]
    res = []
    for i in range(len(row)):
        if row[i] != 0 and row[i] != inf:
            res.append((i, row[i]))
    return res

def GT(graph):
    vnum = len(graph)
    span_forest = [None] * vnum
    def DFS(graph, v0):
        nonlocal span_forest
        for index, weight in graph_outedges(graph, v0):
            if span_forest[index] == None:
                span_forest[index] = (v0, weight)
                DFS(graph, index)
    for i in range(vnum):
        if span_forest[i] == None:
            span_forest[i] = (i, 0)
            DFS(graph, i)
    return span_forest


if __name__ == '__main__':
    test = [[0, 1, 1, 1, inf, inf, inf], [1, 0, inf, 1, 1, inf, 1], \
            [1, inf, 0, 1, inf, 1, inf], [1, 1, 1, 0, inf, inf, 1],\
            [inf, 1, inf, inf, 0, inf, 1], [inf, inf, 1, inf, inf, 0, 1],\
            [inf, 1, inf, 1, 1, 1, 0]]
    k = GT(test)
    print(k)
        
