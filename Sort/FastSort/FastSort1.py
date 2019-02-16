class FastSort():
    def __init__(self, elems = []):
        self._elems = elems

    def fs(self, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        if self._elems[low] <= self._elems[high] <= self._elems[mid] \
                or self._elems[mid] <= self._elems[high] <= self._elems[low]:
            pivot = self._elems[high]
        elif self._elems[low] <= self._elems[mid] <= self._elems[high] \
                or self._elems[high] <= self._elems[mid] <= self._elems[low]:
            pivot = self._elems[mid]
        elif self._elems[mid] <= self._elems[low] <= self._elems[high] \
                or self._elems[high] <= self._elems[low] <= self._elems[mid]:
            pivot = self._elems[low]
        pivot, self._elems[low] = self._elems[low], pivot
        i, j = low, high
        while i < j:
            while i < j and self._elems[j] > pivot:
                j -= 1
            if i < j:
                self._elems[i] = self._elems[j]
                i += 1
            while i < j and self._elems[i] < pivot:
                i += 1
            if i < j:
                self._elems[j] = self._elems[i]
                j -= 1
        self._elems[i] = pivot
        self.fs(low, i - 1)
        self.fs(i + 1, high)

    def get_res(self):
        return self._elems

if __name__ == '__main__':
    test = [1, 5, 8, 2, 9, 26, 98, 34, 101, 76, 34, 26]
    k1 = FastSort(test)
    k1.fs(0, len(test) - 1)
    print(k1.get_res())
