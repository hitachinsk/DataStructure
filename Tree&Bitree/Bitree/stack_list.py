import ExceptionStack as es

class Stack_list():
    def __init__(self):
        self._elem = []

    def is_empty(self):
        return self._elem == []

    def push(self, elem):
        self._elem.append(elem)

    def top(self):
        if self._elem == []:
            raise es.StackUnderflow('get top in an empty stack.')
        else:
            return self._elem[-1]

    def pop(self):
        if self._elem == []:
            return es.StackUnderflow('pop elems in an empty stack.')
        else:
            e = self._elem[-1]
            self._elem.pop()
            return e

    def print_stack(self):
        length = len(self._elem)
        for i in range(length):
            if i != length - 1:
                print(self._elem[i], end = '->')
            else:
                print(self._elem[i])


#k1 = Stack_list()
#k1.push(3)
#k1.push(5)
#k1.print_stack()
#m = k1.top()
#k1.pop()
#n = k1.top()
#print(m, n)
