#采用邻接矩阵来构造图，但存储形式采用邻接表

class GraphError(ValueError):
    pass

inf = float('inf')

class GraphL():
    def __init__(self, matrix, uncount = 0):
        var = len(matrix)
        for each in matrix:
            if len(each) != var:
                raise GraphError('The matrix is not square')
        self._var = var
        self._uncount = uncount
        self._mat = [self._outline(matrix[i], uncount) for i in range(var)]

    def _outline(self, line, uncount):
        res = []
        for i in range(len(line)):
            if line[i] != uncount and line[i] != inf:
                res.append((i, line[i]))
        return res

    def is_empty(self):
        return self._var == 0

    def vertex_num(self):
        return self._var

    def add_vertex(self):
        self._mat.append([])
        self._var += 1
        return self._var - 1

    def _invalid(self, v):
        return 0 > v or v > self._var - 1
        
    def add_edge(self, vi, vj, val):
        if vi == vj:
            return
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('Invalid vertex cannot be added edges')
        row = self._mat[vi]
        counter = 0
        while counter < len(row):
            if row[counter][0] < vj:
                counter += 1
                continue
            elif row[counter][0] == vj:
                self._mat[vi][counter][1] = val
                return
            elif row[counter][0] > vj:
                break
        self._mat[vi].insert(counter, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('Invalid vertex cannot exist edges')
        if vi == vj:
            return 0
        row = self._mat[vi]
        for i in range(len(row)):
            if row[i][0] == vj:
                return row[i][1]
        else:
            return inf

    def out_edges(self, v):
        if self._invalid(v):
            raise GraphError('Invalid vertex cannot list edges')
        return self._mat[v]


#test
if __name__ == '__main__':
    test = [[0, 1, 1, inf, 1], [1, 0, 6, inf, 1], [1, 6, 0, 1, inf], \
            [inf, inf, 1, 0, 3], [1, 1, inf, 3, 0]]
    k1 = GraphL(test)
    k1.add_edge(3, 1, 20)
    for m in range(5):
        ui = k1.out_edges(m)
        print(ui)
    m = k1.get_edge(3, 1)
    print(m)
    
        
        
