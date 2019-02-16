#for efficient operation, link realization for stack uses head as bottom of stack
#while list realization uses tail as bottom of stack
#to get O(1) time complexity
import ExceptionStack as es

class LNode():
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

        
class Stack_link():
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top == None

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def top(self):
        if self._top == None:
            raise es.StackUnderflow('get elem on the empty stack')
        else:
            return self._top.elem

    def pop(self):
        if self._top == None:
            raise es.StackUnderflow('pop elem on the empty stack')
        else:
            e = self._top.elem
            p = self._top
            self._top = self._top.next
            p.next = None
            return e

    def printall(self):
        p = self._top
        while p:
            if p.next:
                print(p.elem, end = '<-')
            else:
                print(p.elem)
            p = p.next
            


k1 = Stack_link()
k1.push(2)
k1.push(3)
k1.push(5)
k1.printall()
m = k1.top()
k1.pop()
n = k1.top()
print(m, n)
