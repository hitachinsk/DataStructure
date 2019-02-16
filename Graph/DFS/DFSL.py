#邻接表做DFS
import stack_list as sl
def DFSL(graph, v):
    vertex = [0] * len(graph)
    ss = sl.Stack_list()
    ss.push(v)
    DFS_SEQ = []
    while len(DFS_SEQ) != len(graph):
        if ss.is_empty():
            for index in range(len(vertex)):
                if vertex[index] == 0:
                    ss.push(index)
                    break
        location = ss.pop()
        if vertex[location] != 0:
            continue
        vertex[location] = 1
        DFS_SEQ.append(location)
        row = graph[location]
        for i in range(len(row)):
            if vertex[row[i][0]] == 0:
                if i + 1 < len(row):
                    ss.push(row[i + 1][0])
                ss.push(row[i][0])
                break
    return DFS_SEQ



if __name__ == '__main__':
    test = [[(1, 1), (2, 1), (3, 1)], [(0, 1), (3, 1), (4, 1), (6, 1)],\
            [(0, 1), (3, 1), (5, 1)], [(0, 1), (1, 1), (2, 1), (6, 1)],\
            [(1, 1), (6, 1)], [(2, 1), (6, 1)], [(1, 1), (3, 1), (4, 1), (5, 1)]]
    k = DFSL(test, 0)
    print(k)
