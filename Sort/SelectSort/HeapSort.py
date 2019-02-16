class HeapSort():
    def __init__(self, elems = []):
        self._elems = elems

    def HS(self):
        mid = len(self._elems) // 2
        for i in range(mid, -1, -1):
            self._sift_down(self._elems[i], i, len(self._elems))
        for i in range(len(self._elems) - 1, -1, -1):
            self._elems[0], self._elems[i] = self._elems[i], self._elems[0]
            self._sift_down(self._elems[0], 0, i)

    def _sift_down(self, factor, start, end):
        i, j = start, 2 * start + 1
        while j < end:
            if j + 1 < end and self._elems[j] > self._elems[j + 1]:
                j += 1
            if self._elems[i] > self._elems[j]:
                self._elems[i], self._elems[j] = self._elems[j], self._elems[i]
                i = j
                j = 2 * j + 1
            else:
                break
        self._elems[i] = factor

    def get_res(self):
        return self._elems

if __name__ == '__main__':
    test = [1, 5, 8, 2, 101, 26, 76, 34, 9, 98, 34, 26]
    k1 = HeapSort(test)
    k1.HS()
    print(k1.get_res())