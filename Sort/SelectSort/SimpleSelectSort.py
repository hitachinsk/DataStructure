class SimpleSelectSort():
    def __init__(self, elems = []):
        self._elems = elems

    def SSS(self):
        for i in range(len(self._elems) - 1):
            index = i
            for j in range(i, len(self._elems)):
                if self._elems[index] > self._elems[j]:
                    index = j
            if index != i:
                self._elems[index], self._elems[i] = self._elems[i], self._elems[index]

    def get_res(self):
        return self._elems

if __name__ == '__main__':
    test = [1, 5, 8, 2, 9, 26, 98, 34, 101, 76, 34, 26]
    k1 = SimpleSelectSort(test)
    k1.SSS()
    print(k1.get_res())
