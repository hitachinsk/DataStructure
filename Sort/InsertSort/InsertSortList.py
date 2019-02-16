#Worst condition is O(n^2), while the best condition is O(n)
#Space complex extent is O(1)
class InsertSortList():
    def __init__(self, elems = []):
        self._elems = elems

    def InsertSortLowercase(self):
        for i in range(1, len(self._elems)):
            x = self._elems[i]
            j = i
            while j > 0 and self._elems[j - 1] > x:
                self._elems[j] = self._elems[j - 1]
                j -= 1
            self._elems[j] = x

    def InsertSortUppercase(self):
        for i in range(len(self._elems) - 1, -1, -1):
            x = self._elems[i]
            j = i
            while j < len(self._elems) - 1 and self._elems[j + 1] < x:
                self._elems[j] = self._elems[j + 1]
                j += 1
            self._elems[j] = x

    def get_res(self):
        return self._elems

if __name__ == '__main__':
    test = [1, 5, 8, 2, 9, 26, 98, 34, 101, 76, 34, 26]
    k1 = InsertSortList(test)
    k1.InsertSortUppercase()
    print(k1.get_res())