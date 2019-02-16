import link_queue as lq

def BFSL(graph, v):
    q = lq.Linkqueue()
    vertex = [0] * len(graph)
    vertex[v] = 1
    q.enqueue(v)
    BFS_SEQ = [[v]]
    while vertex != [1] * len(graph):
        location = q.dequeue()
        row = graph[location]
        counter = 0
        temp = []
        for each in row:
            if vertex[each[0]] == 0:
                temp.append(each[0])
                q.enqueue(each[0])
                vertex[each[0]] = 1
                counter += 1
        for each in BFS_SEQ:
            if each[-1] == location:
                while counter > 0:
                    if counter != 1:
                        s = each[:]
                        s.append(temp[counter - 1])
                        BFS_SEQ.append(s)
                    else:
                        each.append(temp[counter - 1])
                    counter -= 1
                break
    return BFS_SEQ


if __name__ == '__main__':
    test = [[(1, 1), (2, 1), (3, 1)], [(0, 1), (3, 1), (4, 1), (6, 1)],\
            [(0, 1), (3, 1), (5, 1)], [(0, 1), (1, 1), (2, 1), (6, 1)],\
            [(1, 1), (6, 1)], [(2, 1), (6, 1)], [(1, 1), (3, 1), (4, 1), (5, 1)]]
    k = BFSL(test, 0)
    print(k)

    
