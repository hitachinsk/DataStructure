class DLnode():
    def __init__(self, elem, next_ = None, prev = None):
        self.elem = elem
        self.next = next_
        self.prev = prev


class DList():
    def __init__(self):
        self._head = None
        self._rear = None
        self._length = 0

    def prepand(self, elem):
        p = DLnode(elem)
        if not self._head:
            self._head = p
            self._rear = p
        else:
            p.next = self._head
            self._head.prev = p
            self._head = p
        self._length += 1

    def append(self, elem):
        p = DLnode(elem)
        if not self._head:
            self._head = p
            self._rear = p
        else:
            p.prev = self._rear
            self._rear.next = p
            self._rear = p
        self._length += 1

    def pop(self):
        if not self._head:
            raise ValueError
        if self._head == self._rear:
            self._head = None
            self._rear = None
        else:
            p = self._head
            self._head = self._head.next
            p.next = None
            self._head.prev = None
        self._length -= 1

    def pop_last(self):
        if not self._head:
            raise ValueError
        if self._head == self._rear:
            self._head = None
            self._rear = None
        else:
            p = self._rear
            self._rear = self._rear.prev
            self._rear.next = None
            p.prev = None
        self._length -= 1

    def isEmpty(self):
        return not self._head

    def find(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p:
            print(p.elem, end = '')
            if p.next:
                print(',', end = '')
            p = p.next
        print('')
