#这里，队列默认从大到小排序，每次弹出元素都从列表末尾弹出（弹出最小元素）
class PriorQueueError(ValueError):
    pass

class Prior_queue_list():
    def __init__(self, elem = []):
        self._elem = elem
        #从大到小排序
        self._elem.sort(reverse = True)

    def is_empty(self):
        return len(self._elem) == 0

    def enqueue(self, key):
        length = len(self._elem)
        for i in range(length):
            if self._elem[i] <= key:
                self._elem.insert(i, key)
                break
        else:
            self._elem.append(key)

    def dequeue(self):
        if not self._elem:
            raise PriorQueueError('cannot delete elems in an empty queue')
        else:
            e = self._elem[-1]
            self._elem.pop()
            return e

    def peek(self):
        if not self._elem:
            raise PriorQueueError('cannot get an elem from an empty queue')
        else:
            e = self._elem[-1]
            return e

    def printall(self):
        for i in range(len(self._elem)):
            if i == len(self._elem) - 1:
                print(self._elem[i])
                break
            print(self._elem[i], end = '->')


if __name__ == '__main__':
    k = Prior_queue_list([2,6,4,7,3,9])
    k.printall()
    k.enqueue(5)
    k.printall()
    k.dequeue()
    k.printall()
    m = k.peek()
    print(m)
            
