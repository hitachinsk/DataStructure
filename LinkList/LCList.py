import LLClass as LC

class LCList():
    def __init__(self):
        self._rear = None
        self._length = 0

    def isEmpty(self):
        return self._rear is None

    def prepand(self, elem):
        p = self._rear
        if not p:
            p = LC.Lnode(elem)
            self._rear = p
            self._rear.next = self._rear
        else:
            self._rear.next = LC.Lnode(elem, p.next)

    def append(self, elem):
        self.prepand(elem)
        self._rear = self._rear.next

    def pop(self):
        if not self._rear:
            raise LC.Verror('pop uses in null link')
        p = self._rear
        if p.next == p:
            self._rear = None
            e = p.elem
        else:
            e = p.next.elem
            p.next = p.next.next
        return e

    def pop_last(self):
        if not self._rear:
            raise LC.Verror('pop uses in null link')
        p = self._rear
        if p.next == p:
            self._rear = None
            e = p.elem
        else:
            while p:
                if p.next == self._rear:
                    break
                p = p.next
            e = p.next.elem
            p.next = p.next.next
            self._rear = p

    def printall(self):
        p = self._rear
        if p:
            while p:
                if p.next == self._rear:
                    print(p.elem, end = '')
                    break
                print(str(p.elem) + ',', end = '')
                p = p.next

                
            
