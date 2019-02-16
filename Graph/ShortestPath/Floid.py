#copy from page 254
inf = float('inf')
def all_shortest_paths(graph):
    vnum = len(graph)
    a = graph
    nvertex = [[-1 if a[i][j] == inf else j for j in range(vnum)]\
               for i in range(vnum)]

    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nvertex[i][j] = a[i][k] + a[k][j]
    return (a, nvertex)



if __name__ == '__main__':
    test = [[0, inf, 5, 2, inf, inf, inf], [11, 0, 4, inf, inf, 4, inf],\
            [inf, 3, 0, inf, 2, 7, inf], [inf, inf, inf, 0, inf, inf, inf],\
            [inf, inf, inf, inf, 0, inf, 2], [inf, inf, inf, inf, inf, 0, 3],\
            [inf, inf, inf, inf, inf, inf, 0]]
    s = all_shortest_paths(test)
    print(s)
