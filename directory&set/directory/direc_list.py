import Assoc as As


class DictList():
    def __init__(self, elem = None):
        """

        :type elem: As.Assoc
        """
        if elem is None:
            elem = []
        for i in range(len(elem)):
            if not isinstance(elem[i], As.Assoc):
                raise ValueError('The value of elem is not the right type')
        self._elem = elem
        self._sort()

    def _sort(self):
        for i in range(len(self._elem) - 1, -1, -1):
            flag = False
            for j in range(i):
                if self._elem[j] > self._elem[j + 1]:
                    self._elem[j], self._elem[j + 1] = self._elem[j + 1], self._elem[j]
                    flag = True
            if flag is False:
                return

    def is_empty(self):
        return self._elem == []

    def num(self):
        return len(self._elem)

    def search(self, key):
        low, high = 0, len(self._elem) - 1
        if low == high:
            if self._elem[low].key == key:
                print('Target elem has been found')
                print(str(self._elem[medium]))
                return True
        while low < high:
            medium = (low + high) // 2
            if key < self._elem[medium].key:
                high = medium - 1
            elif key > self._elem[medium].key:
                low = medium + 1
            else:
                print('Target elem has been found')
                print(str(self._elem[medium]))
                return True
        print('Target has not been found')
        return False

    def insert(self, key, value):
        temp = As.Assoc(key, value)
        for i in range(len(self._elem)):
            if temp < self._elem[i]:
                self._elem.insert(i, temp)
                return
        self._elem.append(temp)
        return

    def delete(self, key):
        low, high = 0, len(self._elem) - 1
        if low == high:
            if self._elem[low].key == key:
                self._elem = []
        while low < high:
            medium = (low + high) // 2
            if key < self._elem[medium].key:
                high = medium - 1
            elif key > self._elem[medium].key:
                low = medium + 1
            else:
                self._elem.pop(medium)
                return True
        return False

    def values(self):
        for i in range(len(self._elem)):
            yield self._elem[i].value

    def entries(self):
        for i in range(len(self._elem)):
            yield (self._elem[i].key, self._elem[i].value)


# for test
if __name__ == '__main__':
    k1 = As.Assoc(2, 20)
    k2 = As.Assoc(6, 60)
    k3 = As.Assoc(7, 70)
    k4 = As.Assoc(9, 90)
    k5 = As.Assoc(18, 230)
    k6 = As.Assoc(4, 34)
    k7 = As.Assoc(7, 26)
    k8 = As.Assoc(10, 35)
    test = [k1, k2, k3, k4, k5, k6, k7, k8]
    temp = DictList(test)
    temp.insert(20, 9)
    temp.delete(5)
    for m in temp.values():
        print(m)
    m = temp.search(4)
