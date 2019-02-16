import link_queue as lq
import stack_list as sl

#这里构造的是二叉树nodes。
class BinTNodes():
    def __init__(self, elem, left = None, right = None):
        self.elem = elem
        self.left = left
        self.right = right

class Bitree_link():
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root == None

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self, Tree):
        self._root = Tree

    def set_leftchild(self, left):
        self._root.left = left

    def set_rightchild(self, right):
        self._root.right = right

    def preorder_itetator(self):
        ss = sl.Stack_list()
        while t or not ss.is_empty():
            while t:
                yield t.elem
                ss.push(t.right)
                t = t.left
            t = ss.pop()

    def printall(self):
        q = lq.Linkqueue()
        q.enqueue(self._root)
        while not q.is_empty():
            temp = q.dequeue()
            print(temp.elem, end = ',')
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)

def count_BinTNodes(t):
    if not t:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinNodes(t.right)

def sum_BinTNodes(t):
    if not t:
        return 0
    else:
        return t.elem + sum_BinTNodes(t.left) + sum_BinTNodes(t.right)

def preorder(t, proc):
    if not t:
        return
    else:
        proc(t.elem)
        preorder(t.left)
        preorder(t.right)

def midorder(t, proc):
    if not t:
        return
    else:
        midorder(t.left)
        proc(t.elem)
        midorder(t.right)

def postorder(t, proc):
    if not t:
        return
    else:
        postorder(t.left)
        postorder(t.right)
        proc(t.elem)

def print_BinTNodes(t):
    if not t:
        print('^', end = '')
        return
    else:
        print('(' + str(t.elem), end = '')
        print_BinTNodes(t.left)
        print_BinTNodes(t.right)
        print(')', end = '')

def levelorder(t, proc):
    if not t:
        return
    else:
        q = lq.Linkqueue()
        q.enqueue(t)
        while not q.is_empty():
            temp = q.dequeue()
            proc(temp.elem)
            if temp.left:
                q.enqueue(temp.left)
            if temp.right:
                q.enqueue(temp.right)

def preorder_nonrec(t, proc):
    ss = sl.Stack_list()
    while t or not ss.is_empty():
        while t:
            proc(t.elem)
            ss.push(t.right)
            t = t.left
        t = ss.pop()

def midorder_nonrec(t, proc):
    ss = sl.Stack_list()
    while t or not ss.is_empty():
        while t:
            ss.push(t)
            t = t.left
        t = ss.pop()
        proc(t.elem)
        if t.right and not ss.is_empty():
            t = t.right
        else:
            #强制退栈技术
            t = None

def postorder_nonrec(t, proc):
    ss = sl.Stack_list()
    while t or not ss.is_empty():
        while t:
            ss.push(t)
            if t.left:
                ss.push(t.left)
            else:
                ss.push(t.right)
        t = ss.pop()
        proc(t.elem)
        if s.top().left == t and not ss.is_empty():
            t = s.top().right
        else:
            t = None

if __name__ == '__main__':
    temp = Bitree_link()
    t = BinTNodes(3, BinTNodes(4, BinTNodes(6, BinTNodes(10), BinTNodes(90))), BinTNodes(5))
    temp.set_root(t)
    temp.printall()
    
    








            
            
            
