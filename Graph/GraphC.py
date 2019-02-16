#采用邻接矩阵来创建图类
class GraphError(ValueError):
    pass

inf = float('inf')

#无向图
class GraphC():
    def __init__(self, matrix = [], uncount = 0):
        var = len(matrix)
        for each in matrix:
            if len(each) != var:
                raise GraphError('The matrix you inputted is not a square matrix')
        for m in range(var):
            for n in range(var):
                if matrix[m][n] != matrix[n][m]:
                    raise GraphError('The link matrix is not reciprocal')
                if m == n:
                    if matrix[m][n] != uncount:
                        raise GraphError('The diagnal elems are not uncount')
        self._mat = [matrix[i][:] for i in range(var)]
        self._uncount = uncount
        self._var = var

    def is_empty(self):
        return self._var == 0

    def _invalid(self, v):
        return 0 > v or v > self._var

    def vertex_num(self):
        return self._var

    def add_vertex(self, elem):
        temp = elem[:]
        if len(temp) != self._var + 1:
            raise GraphError('The dimension of elem is wrong')
        counter = 0
        while counter < self._var:
            self._mat[counter].append(temp[counter])
            counter += 1
        self._mat.append(temp)
        self._var += 1

    def add_edge(self, vi, vj, val = 1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('The index of vertex is out od range')
        if vi == vj:
            return
        self._mat[vi][vj] = val
        self._mat[vj][vi] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('The index of vertex is out of range, we cannot get egde')
        return self._mat[vi][vj]

    def out_edges(self, v):
        res = []
        if self._invalid(v):
            raise GraphError('Cannot give eages of a unleagle vertex')
        for index in range(self._var):
            if self._mat[v][index] != self._uncount and self._mat[v][index] != inf:
                res.append((index, self._mat[v][index]))
        return res

#有向图
class GraphC_direction(GraphC):
    def __init__(self, matrix = [], uncount = 0):
        var = len(matrix)
        for each in matrix:
            if len(each) != var:
                raise GraphError('The matrix you inputted is not a square matrix')
        self._mat = [matrix[i][:] for i in range(var)]
        self._uncount = uncount
        self._var = var

    def add_vertex(self, elem_out, elem_in):
        temp_out = elem_out[:]
        temp_in = elem_in[:]
        if temp_out[-1] != temp_in[-1]:
            raise GraphError('Out_line and in_line do not match') 
        if len(temp_out) != self._var + 1 or len(temp_in) != self._var + 1:
            raise GraphError('The dimension of elem is wrong')
        counter = 0
        while counter < self._var:
            self._mat[counter].append(temp_in[counter])
            counter += 1
        self._mat.append(temp_out)
        self._var += 1

    def add_edge(self, vi, vj, val = 1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError('The index of vertex is out od range')
        if vi == vj:
            return
        self._mat[vi][vj] = val


#test
def test_graphc():
    temp = [[0, 1, 1, inf], [1, 0, 1, inf], [1, 1, 0, 1], [inf, inf, 1, 0]]
    t1 = GraphC(temp)
    k = t1.is_empty()
    m = t1.vertex_num()
    print(k, m)
    t1.add_edge(2, 1, 6)
    s = t1.get_edge(1, 2)
    print(s)
    d = t1.out_edges(2)
    print(d)
    elem = [1, 1, inf, 3, 0]
    t1.add_vertex(elem)
    for k1 in range(5):
        ui = t1.out_edges(k1)
        print(ui)

def test_graphc_dire():
    temp = [[0, 2, inf], [inf, 0, 3], [inf, inf, 0]]
    t1 = GraphC_direction(temp)
    t1.add_edge(2, 1, 6)
    elem_out = [2, 3, 6, 0]
    elem_in = [inf, inf, 4, 0]
    t1.add_vertex(elem_out, elem_in)
    for k1 in range(4):
        ui = t1.out_edges(k1)
        print(ui)
        
if __name__ == '__main__':
    test_graphc_dire()
        
        
            
        

