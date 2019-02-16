import Bitree_link as bl
import Prior_queue_heap as pq
import link_queue as lq
#solve 2 problems, the build of HuffmanTree and HuffmanCode
class HFNodes(bl.BinTNodes):
    def __lt__(self, another):
        return self.elem < another.elem


class HFPriorQueue(pq.Prior_queue_heap):
    def printall(self):
        for i in range(len(self._elem)):
            if i == len(self._elem) - 1:
                break
            print(self._elem[i].elem, end = '->')
    def depth(self):
        return len(self._elem)


def build_HFTree(elems = []):
    if len(elems) == 0:
        return
    for each in elems:
        if not isinstance(each, HFNodes):
            raise ValueError('All elements must be type of HFNodes')
    temp = HFPriorQueue(elems)
    while temp.depth() != 1:
        k1 = temp.dequeue()
        k2 = temp.dequeue()
        c = HFNodes(k1.elem + k2.elem, k1, k2)
        temp.enqueue(c)

    c = temp.dequeue()
    printTree(c)
    return c

def printTree(c):
    ss = lq.Linkqueue()
    ss.enqueue(c)
    while not ss.is_empty():
        element = ss.dequeue()
        print(element.elem, end = '->')
        if element.left:
            ss.enqueue(element.left)
        if element.right:
            ss.enqueue(element.right)

#direc表示的是映射的字典
def HuffmanCode(t, direc):
    if not t:
        return
    ss = lq.Linkqueue()
    res = []
    t.elem = ''
    ss.enqueue(t)
    while not ss.is_empty():
        temp = ss.dequeue()
        if temp.left and not_leaf(temp.left):
            temp.left.elem = temp.elem + '0'
            ss.enqueue(temp.left)
        if temp.right and not_leaf(temp.right):
            temp.right.elem = temp.elem + '1'
            ss.enqueue(temp.right)
        if temp.left and not not_leaf(temp.left):
            for each in direc:
                if direc[each] == temp.left.elem:
                    store = each
                    direc.pop(store)
                    break
            code = temp.elem + '0'
            res.append((store, code))
                    
        if temp.right and not not_leaf(temp.right):
            for each in direc:
                if direc[each] == temp.right.elem:
                    store = each
                    direc.pop(store)
                    break
            code = temp.elem + '1'
            res.append((store, code))
    return res

def not_leaf(t):
    if t.left or t.right:
        return True
    else:
        return False
        


if __name__ == '__main__':
    elems = {'a':10, 'b':18, 'c':8, 'd':4, 'e':65, 'f':37, 'g':29}
    k = []
    for each in elems:
        k.append(HFNodes(elems[each]))
    s = build_HFTree(k)
    final = HuffmanCode(s, elems)
    print('')
    for each in final:
        print(each)
    
    
    
