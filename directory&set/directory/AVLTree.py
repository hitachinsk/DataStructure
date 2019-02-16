import Assoc as As
import SortBiTree as sb

class AVLnode():
    def __init__(self, key, value):
        self.node = As.Assoc(key, value)
        self.left = None
        self.right = None
        self.bf = 0

class AVLTree(sb.SortBiTree):
    #a是最小非平衡子树的根，b是a的左或右子节点
    def LL(self, a, b):
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    def LR(self, a, b):
        c = b.right
        temp = c.bf
        b.right = c.left
        a.left = c.right
        c.left = b
        c.right = a
        c.bf = 0
        if temp == 1:
            b.bf = 0
            a.bf = -1
        elif temp == -1:
            b.bf = 1
            a.bf = 0
        else:
            a.bf = b.bf = 0
        return c

    def RL(self, a, b):
        c = b.left
        temp = c.bf
        b.left = c.right
        a.right = c.left
        c.right = b
        c.left = a
        c.bf = 0
        if temp == 1:
            b.bf = -1
            a.bf = 0
        elif temp == -1:
            b.bf = 0
            a.bf = 1
        else:
            a.bf = b.bf = 0
        return c

    def RR(self, a, b):
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    def insert(self, key, value):
        #a是最小非平衡子树的根节点
        #pa为a的父节点，q为p的父节点
        pa = q = None
        a = p = self._root
        #d记录插入节点子树方向
        #1为左子树，-1为右子树
        d = 0
        if not p:
            self._root = AVLnode(key, value)
            return
        while p:
            if key == p.node.key:
                p.node.value = value
                return
            if p.bf != 0:
                pa, a = q, p
            q = p
            if key < p.node.key:
                p = p.left
            else:
                p = p.right
        temp = AVLnode(key, value)
        if key < q.node.key:
            q.left = temp
        else:
            q.right = temp
        if key < a.node.key:
            p = b = a.left
            d = 1
        else:
            p = b = a.right
            d = -1
        while p != temp:
            if key < p.node.key:
                p.bf = 1
                p = p.left
            else:
                p.bf = -1
                p = p.right
        if d == 1:
            if b.bf == 1:
                root = self.LL(a, b)
            else:
                root = self.LR(a, b)
        else:
            if b.bf == 1:
                root = self.RL(a, b)
            else:
                root = self.RR(a, b)
        if a == self._root:
            self._root = root
            return
        else:
            if pa.node.key > root.node.key:
                pa.left = root
            else:
                pa.right = root




    def delete(self, key):
        pass


def buildTree(elems):
    for each in elems:
        if not isinstance(each, As.Assoc):
            raise ValueError('The elems are not Assoc type')
    res = AVLTree()
    for each in elems:
        res.insert(each.key, each.value)
    return res

if __name__ == '__main__':
    test = [As.Assoc(2, 32), As.Assoc(18, 27), As.Assoc(7, 14), As.Assoc(12, 6),
            As.Assoc(5, 18), As.Assoc(8, 11), As.Assoc(15, 3), As.Assoc(23, 0)]

    tree = buildTree(test)
    tree.print()