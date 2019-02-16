class Lnode():
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

class LinkList():
    def __init__(self):
        self._root = None

    def append(self, elem):
        if not self._root:
            self._root = Lnode(elem)
        else:
            p = self._root
            while p.next:
                p = p.next
            p.next = Lnode(elem)

    def Link2List(self):
        res = []
        p = self._root
        while p:
            res.append(p.elem)
            p = p.next
        return res

    def get_head(self):
        return self._root

    def modify(self, p):
        self._root = p


class BasicSortLink():
    def __init__(self, elems = []):
        if elems == []:
            raise ValueError
        k = len(elems[0])
        for each in elems:
            if not (isinstance(each, tuple) or isinstance(each, list)):
                raise ValueError('The type of elems is not all iterable')
            if len(each) != k:
                raise ValueError('The length of elems are not the same')
        self._elems = LinkList()
        for i in range(len(elems)):
            self._elems.append(elems[i])
        self._slen = k

    def BasicSortLink(self, r):
        store = [LinkList() for i in range(r)]
        b = self._slen
        counter = -1
        while counter >= -b:
            p = self._elems.get_head()
            while p:
                q = p.next
                kd = store[p.elem[counter]].get_head()
                if kd == None:
                    store[p.elem[counter]].modify(p)
                else:
                    while kd.next:
                        kd = kd.next
                    kd.next = p
                p.next = None
                p = q
            for i in range(len(store) - 1):
                front, rear = store[i].get_head(), store[i + 1].get_head()
                while front and front.next:
                    front = front.next
                if front:
                    front.next = rear
            self._elems.modify(store[0].get_head())
            for each in store:
                each.modify(None)
            counter -= 1


    def get_res(self):
        return self._elems.Link2List()

if __name__ == '__main__':
    test = [(1, 3, 2), (3, 1, 3), (2, 2, 0), (0, 1, 1), (2, 0, 2), (3, 0, 1), (0, 3, 2),
            (1, 0, 3), (0, 2, 0), (2, 1, 1), (3, 1, 0), (2, 0, 1), (1, 1, 0), (0, 1, 3),
            (2, 3, 1), (2, 3, 1), (0, 2, 2), (0, 3, 0), (3, 3, 1), (2, 1, 3), (3, 1, 1)]
    k = BasicSortLink(test)
    k.BasicSortLink(4)
    print(k.get_res())
