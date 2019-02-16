import Prior_queue_heap as ph

inf = float('inf')
def SGT_prim(graph):
    q = ph.Prior_queue_heap()
    vnum = len(graph)
    spring = [None] * vnum
    spring[0] = (0, 0)
    i = 0
    flag = True
    while (None in spring) and (not q.is_empty()):
        if flag == True:
            edges = outline(graph, i)
            for each in edges:
                q.enqueue(each)
        temp = q.dequeue()
        if spring[temp[1]] == None:
            spring[temp[1]] = (i, temp[0])
            i = temp[1]
            flag = True
        else:
            flag = False
    if None not in spring:
        return spring
    else:
        return False

def outline(graph, v):
    row = graph[v]
    res = []
    for i in range(len(row)):
        if row[i] != 0 and row[i] != inf:
            res.append((row[i], i))
    return res


        
if __name__ == '__main__':
    test = [[0, 2, 5, 7, inf, inf, inf], [2, 0, inf, 4, 12, inf, 5], \
            [5, inf, 0, 8, inf, 13, inf], [7, 4, 8, 0, inf, inf, 3],\
            [inf, 12, inf, inf, 0, inf, 7], [inf, inf, 13, inf, inf, 0, 15],\
            [inf, 5, inf, 3, 7, 15, 0]]
    k = SGT_prim(test)
    print(k)
