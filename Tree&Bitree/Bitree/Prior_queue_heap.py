#用堆实现的优先队列（这种操作的时间复杂度可以达到O(logn))
class PriorQueueError(ValueError):
    pass

class Prior_queue_heap():
    def __init__(self, elem = []):
        if not elem:
            self._elem = []
        else:
            self._elem = list(elem)
            #将实际存在的elem变成一个堆，本质是一种筛选
            self.makeheap()

    def is_empty(self):
        return self._elem == None

    #优先队列的入队列过程实质是一次向上筛选
    def enqueue(self, key):
        self._elem.append(key)
        i = len(self._elem) - 1
        j = (i - 1) // 2
        while i > 0 and self._elem[i] < self._elem[j]:
            self._elem[i] = self._elem[j]
            i = j
            j = (i - 1) // 2
            self._elem[i] = key
        self._elem[i] = key

    def dequeue(self):
        if not self._elem:
            raise PriorQueueError('cannot delete an elem from an empty queue.')
        e = self._elem[0]
        wp = self._elem[-1]
        self._elem.pop()
        if not self._elem:
            return wp
        self._elem[0] = wp
        i= 0
        j = 2 * i + 1
        while j < len(self._elem):
            #compare between siblings
            if j + 1 < len(self._elem) and self._elem[j] > self._elem[j + 1]:
                j = j + 1
            if wp < self._elem[j]:
                break
            self._elem[i] = self._elem[j]
            i = j
            j = 2 * i + 1
        self._elem[i] = wp
        return e

    def peek(self):
        if not self._elem:
            raise PriorQueueError('cannot get an elem from an empty queue.')
        else:
            e = self._elem[0]
            return e

    def makeheap(self):
        end = len(self._elem)
        for i in range(end // 2, -1, -1):
            self._siftdown(i, end)

    def _siftdown(self, start, end):
        wp = self._elem[start]
        i, j = start, 2 * start + 1
        while j < end:
            #compare between siblings
            if j + 1 < end and self._elem[j] > self._elem[j + 1]:
                j = j + 1
            if wp < self._elem[j]:
                break
            self._elem[i] = self._elem[j]
            i = j
            j = 2 * i + 1
        self._elem[i] = wp

    def printall(self):
        for i in range(len(self._elem)):
            if i == len(self._elem) - 1:
                print(self._elem[i])
                break
            print(self._elem[i], end = '->')


if __name__ == '__main__':
    temp = Prior_queue_heap([3,5,8,6,9,4,7])
    temp.printall()
    temp.enqueue(5.5)
    temp.printall()
    temp.dequeue()
    temp.printall()
    temp.enqueue(2)
    temp.printall()
    temp.dequeue()
    temp.printall()
    
        
            
        
        
