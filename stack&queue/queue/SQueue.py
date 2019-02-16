import link_queue as lq
#The realization of loop queue
#self._head supports dequeue
#self._head + self._num supports enqueue
class SQueue():
    def __init__(self, len_ = 8):
        self._head = 0
        self._len = len_
        self._elem = [0] * self._len
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def enqueue(self, elem):
        if self._num == self._len:
            self._extend()
        self._elem[(self._head + self._num) % self._len] = elem
        self._num += 1

    def _extend(self):
        new_len = self._len * 2
        old_len = self._len
        new_elem = [0] * new_len
        for i in range(old_len):
            new_elem[i] = self._elem[(self._head + i) % old_len]
        self._head = 0
        self._len = new_len
        self._elem = new_elem
            
    def dequeue(self):
        if self._num <= 0:
            raise lq.QueueUnderflow('cannot delete an elem in an empty queue.')
        else:
            e = self._elem[self._head]
            self._elem[self._head] = 0
            self._head += 1
            self._num -= 1
            return e

    def peek(self):
        if self._num <= 0:
            raise lq.QueueUnderflow('cannot get elem in an empty queue.')
        else:
            e = self._elem[self._head]
            return e

    def printall(self):
        p = self._head
        for i in range(self._num):
            if i != self._num - 1:
                print(self._elem[p + i], end = '->')
            else:
                print(self._elem[p + i])


if __name__ == '__main__':
    temp = SQueue()
    temp.enqueue(2)
    temp.enqueue(3)
    temp.enqueue(5)
    temp.enqueue(7)
    temp.enqueue(2)
    temp.enqueue(3)
    temp.enqueue(5)
    temp.enqueue(7)
    temp.enqueue(7)
    temp.printall()
    k = temp.dequeue()
    print(k)
    temp.printall()
    m = temp.peek()
    print(m)
    temp.printall()
    temp.enqueue(9)
    temp.printall()
        
