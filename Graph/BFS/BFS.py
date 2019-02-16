#BFS遍历图，采用邻接矩阵作为图的存储结构
import link_queue as lq
inf = float('inf')
def BFS(graph, v):
    q = lq.Linkqueue()
    vertex = [0] * len(graph)
    BFS_SEQ = []
    vertex[v] = 1
    BFS_SEQ.append([v])
    q.enqueue(v)
    while vertex != [1] * len(graph):
        if q.is_empty():
            for j in range(len(vertex)):
                if vertex[j] == 0:
                    vertex[j] = 1
                    q.enqueue(j)
                    break
        location = q.dequeue()
        row = graph[location]
        counter = 0
        temp = []
        for i in range(len(row)):
            if vertex[i] == 0 and row[i] != 0 and row[i] != inf:
                temp.append(i)
                vertex[i] = 1
                q.enqueue(i)
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
    test = [[0, 1, 1, 1, inf, inf, inf], [1, 0, inf, 1, 1, inf, 1], \
            [1, inf, 0, 1, inf, 1, inf], [1, 1, 1, 0, inf, inf, 1],\
            [inf, 1, inf, inf, 0, inf, 1], [inf, inf, 1, inf, inf, 0, 1],\
            [inf, 1, inf, 1, 1, 1, 0]]
    k = BFS(test, 0)
    print(k)
