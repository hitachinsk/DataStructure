#列表实现二叉树
#列表每一个元素都由3个元素组成，[root, left, right]

class BitreeError(ValueError):
    pass



class Bitree_list():
    def __init__(self, elem = []):
        if self._check(elem):
            self._elem = elem
        else:
            raise BitreeError('length of elem is not 3')

    def is_empty(self):
        return len(self._elem)

    def root(self):
        return self._elem[0]

    def left(self):
        return self._elem[1]

    def right(self):
        return self._elem[2]

    def set_root(self, data):
        self._elem[0] = data

    def set_left(self, left):
        self._elem[1] = left

    def set_right(self, right):
        self._elem[2] = right

    def _check(self, elem):
        if ((not isinstance(elem[1], list)) and (not isinstance(elem[2], list))):
            if (isinstance(elem[0], int) or isinstance(elem[0], float)) and len(elem) == 3 and (elem[1] == None or elem[1] == True) and (elem[2] == None or elem[2] == True):
                return True
            else:
                return False
        else:
            for i in range(3):
                if isinstance(elem[i], list):
                    m = self._check(elem[i])
                    if m == False:
                        return False
            return True


k = Bitree_list([1, [2, [4, None, None], None], [3, None, None]])
m = k.root()
print(m)
                    
