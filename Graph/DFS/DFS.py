#DFS深度优先搜索一个邻接矩阵结构图
import stack_list as sl
inf = float('inf')
def DFS(graph, v):
    ss = sl.Stack_list()
    vertex = [0] * len(graph)
    ss.push(v)
    DFS_SEQ = []
    while (len(DFS_SEQ) != len(graph)):
        if ss.is_empty():
            for j in range(len(vertex)):
                if vertex[j] == 0:
                    break
            ss.push(j)
        location = ss.pop()
        if vertex[location] != 0:
            continue
        DFS_SEQ.append(location)
        vertex[location] = 1
        temp = 0
        sp = -1
        for i in range(len(graph)):
            if vertex[i] == 0 and graph[location][i] != 0 and \
               graph[location][i] != inf:
                if temp == 0:
                    sp = i
                if temp == 1:
                    ss.push(i)
                temp += 1
                if temp > 1:
                    break
        if sp != -1:
            ss.push(sp)
    return DFS_SEQ

if __name__ == '__main__':
    test = [[0, 1, 1, 1, inf, inf, inf], [1, 0, inf, 1, 1, inf, 1], \
            [1, inf, 0, 1, inf, 1, inf], [1, 1, 1, 0, inf, inf, 1],\
            [inf, 1, inf, inf, 0, inf, 1], [inf, inf, 1, inf, inf, 0, 1],\
            [inf, 1, inf, 1, 1, 1, 0]]
    k = DFS(test, 0)
    print(k)
        
                
                
    
