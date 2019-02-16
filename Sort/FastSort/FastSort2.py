class FastSort2():
    def __init__(self, elems = []):
        self._elems = elems

    def FS2(self, low, high):
        if low >= high:
            return
        i = low
        pivot = self._elems[low]
        for m in range(low + 1, high + 1):
            if self._elems[m] < pivot:
                i += 1
                self._elems[i], self._elems[m] = self._elems[m], self._elems[i]
        self._elems[low], self._elems[i] = self._elems[i], self._elems[low]
        self.FS2(low, i-1)
        self.FS2(i+1, high)

    def get_res(self):
        return self._elems

if __name__ == '__main__':
    test = [1, 5, 8, 2, 9, 26, 98, 34, 101, 76, 34, 26]
    k1 = FastSort2(test)
    k1.FS2(0, len(test) - 1)
    print(k1.get_res())
