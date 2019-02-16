class QueueUnderflow(ValueError):
    pass

class LNode():
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

#add elements at tail, delete at head
class Linkqueue():
    def __init__(self):
        self._head = None
        self._rear = None
        self._counter = 0

    def is_empty(self):
        return self._head == None

    def enqueue(self, elem):
        p = LNode(elem)
        if self._head == None:
            self._head = p
            self._rear = p
            self._counter += 1
        else:
            self._rear.next = p
            self._rear = self._rear.next
            self._counter += 1

    def dequeue(self):
        if self._head == None:
            raise QueueUnderflow('Empty queue cannot delete elements')
        elif self._head.next == None:
            e = self._head.elem
            self._head = None
            self._rear = None
            self._counter -= 1
            return e
        else:
            e = self._head.elem
            p = self._head
            self._head = self._head.next
            p.next = None
            self._counter -= 1
            return e

    def peek(self):
        if self._head == None:
            raise QueueUnderflow('Empty queue cannot get elements')
        else:
            e = self._head.elem
            return e

    def depth(self):
        return self._counter

    def print_queue(self):
        if self._head:
            p = self._head
            while p:
                if p.next:
                    print(p.elem, end = '<-')
                else:
                    print(p.elem)
                p = p.next




if __name__ == '__main__':
    temp = Linkqueue()
    temp.enqueue(3)
    temp.enqueue(4)
    temp.enqueue(5)
    temp.print_queue()
    s = temp.depth()
    print(s)
    m = temp.peek()
    print(m)
    k = temp.dequeue()
    print(k)
    temp.print_queue()
    h = temp.depth()
    print(h)
    
