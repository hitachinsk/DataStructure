import LLClass as LC

class InsertSortLink():
    def __init__(self, elems = []):
        k1 = LC.LList()
        for i in range(len(elems)):
            k1.append(elems[i])
        self._link = k1

    def insert_sort(self):
        p = self._link.get_head()
        q = p.next
        if not p or not q:
            return
        p = q
        q = q.next
        self._link.get_head().next = None
        while p:
            m = self._link.get_head()
            pm = None
            while m and m.elem < p.elem:
                pm = m
                m = m.next
            if m == self._link.get_head():
                p.next = m
                self._link.modify(p)
            else:
                pm.next = p
                p.next = m
            p = q
            if q:
                q = q.next

    def get_res(self):
        self._link.printall()


if __name__ == '__main__':
    test = [1, 5, 8, 2, 9, 26, 98, 34, 101, 76, 34, 26]
    k1 = InsertSortLink(test)
    k1.insert_sort()
    k1.get_res()
