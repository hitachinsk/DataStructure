import Assoc as As

class BiTreeNode():
    def __init__(self, key, value):
        self.node = As.Assoc(key, value)
        self.left = None
        self.right = None


class SortBiTree():
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root == None

    def search(self, key):
        p = self._root
        while p and p.node.key != key:
            if key > p.node.key:
                p = p.right
            elif key < p.node.key:
                p = p.left
        if p:
            return p.node.key, p.node.value
        else:
            print('No elem found')
            return False

    def insert(self, key, value):
        q = None
        p = self._root
        d = 0
        if not p:
            self._root = BiTreeNode(key, value)
            return
        while p:
            if key == p.node.key:
                p.node.value = value
                return
            elif key > p.node.key:
                q = p
                p = p.right
                d = 1
            else:
                q = p
                p = p.left
                d = -1
        if d == 1:
            temp = BiTreeNode(key, value)
            q.right = temp
            return
        elif d == -1:
            temp = BiTreeNode(key, value)
            q.left = temp
            return

    def values(self):
        stack = []
        p = self._root
        stack.append(p)
        while len(stack) != 0:
            while p and p.left:
                p = p.left
                stack.append(p)
            temp = stack.pop()
            yield temp.node.value
            p = temp.right
            if p:
                stack.append(p)

    def entrices(self):
        stack = []
        p = self._root
        stack.append(p)
        while len(stack) != 0:
            while p and p.left:
                p = p.left
                stack.append(p)
            temp = stack.pop()
            yield temp.node.key, temp.node.value
            p = temp.right
            if p:
                stack.append(p)

    def delete(self, key):
        p = self._root
        q = None
        while p:
            if p.node.key == key:
                pl = p.left
                pr = p.right
                if not q:
                    if pl:
                        self._root = pl
                        while pl.right:
                            pl = pl.right
                        pl.right = pr
                    else:
                        self._root = pr
                if q:
                    if q.left == p:
                        q.left = pl
                        if pl:
                            while pl.right:
                                pl = pl.right
                            pl.right = pr
                        else:
                            q.left = pr
                    elif q.right == p:
                        q.right = pl
                        if pl:
                            while pl.right:
                                pl = pl.right
                            pl.right = pr
                        else:
                            q.right = pr
                p.left = None
                p.right = None
                return
            elif p.node.key > key:
                q = p
                p = p.left
            else:
                q = p
                p = p.right
        print('No elem should be deleted')
        return False

    def print(self):
        for k, v in self.entrices():
            print(k, v)

#create initial tree
def buildTree(elems):
    for each in elems:
        if not isinstance(each, As.Assoc):
            raise ValueError('The elems are not Assoc type')
    res = SortBiTree()
    for each in elems:
        res.insert(each.key, each.value)
    return res

if __name__ == '__main__':
    test = [As.Assoc(2, 32), As.Assoc(18, 27), As.Assoc(7, 14), As.Assoc(12, 6),
            As.Assoc(5, 18), As.Assoc(8, 11), As.Assoc(15, 3), As.Assoc(23, 0)]

    tree = buildTree(test)
    tree.insert(18, 45)
    tree.insert(6, 78)
    print(tree.search(9))
    for i in tree.values():
        print(i, end = '->')
    print('')
    tree.delete(12)
    tree.print()


















