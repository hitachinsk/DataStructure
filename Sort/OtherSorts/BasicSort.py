class BasicSort():
    def __init__(self, elems = []):
        if elems == []:
            raise ValueError
        k = len(elems[0])
        for each in elems:
            if not (isinstance(each, tuple) or isinstance(each, list)):
                raise ValueError('The type of elems is not all iterable')
            if len(each) != k:
                raise ValueError('The length of elems are not the same')
        self._elems = elems

    def bs(self, r):
        temp = [[] for i in range(r)]
        b = len(self._elems[0])
        #range(start, stop, [step])
        for j in range(-1, -b - 1, -1):
            for each in self._elems:
                temp[each[j]].append(each)
            counter = 0
            for a in temp:
                for b in a:
                    self._elems[counter] = b
                    counter += 1
            temp = [[] for i in range(r)]
        return self._elems

if __name__ == '__main__':
    test = [(1, 3, 2), (3, 1, 3), (2, 2, 0), (0, 1, 1), (2, 0, 2), (3, 0, 1), (0, 3, 2),
            (1, 0, 3), (0, 2, 0), (2, 1, 1), (3, 1, 0), (2, 0, 1), (1, 1, 0), (0, 1, 3),
            (2, 3, 1), (2, 3, 1), (0, 2, 2), (0, 3, 0), (3, 3, 1), (2, 1, 3), (3, 1, 1)]
    k = BasicSort(test)
    print(k.bs(4))
