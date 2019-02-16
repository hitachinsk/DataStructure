import toposort as tp
inf = float('inf')
def critical_path(graph):
    def outline(line):
        res = []
        for i in range(len(line)):
            if line[i] != 0 and line[i] != inf:
                res.append((i, line[i]))
        return res
    
    def ee_calc(vnum, graph, toposec):
        ee = [0] * vnum
        for i in toposec:
            for v, w in outline(graph[i]):
                if ee[i] + w > ee[v]:
                    ee[v] = ee[i] + w
        return ee

    def le_calc(vnum, graph, toposec, eelast):
        le = [eelast] * vnum
        for i in range(vnum - 2, -1, -1):
            for v, w in outline(graph[i]):
                if le[i] - w < le[v]:
                    le[v] = le[i] - w
        return le

    def crit_link(vnum, graph, ee, le):
        crit_actions = []
        for i in range(vnum):
            for v, w in outline(graph[i]):
                if ee[i] == le[j] - w:
                    crit_actions.append((i, j, w))
        return crit_actions

    toposec = tp.toposort(graph)
    vnum = len(graph)
    if toposec == False:
        return False
    ee = ee_calc(vnum, graph, toposec)
    le = le_calc(vnum, graph, toposec, ee[-1])
    cl = crit_link(vnum, graph, ee, le)
    return cl
