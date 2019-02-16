class Bubble():
    def __init__(self, elems = []):
        self._elems = elems

    def bubble(self):
        for i in range(len(self._elems)):
            flag = False
            for j in range(len(self._elems) - 1 - i):
                if self._elems[j] > self._elems[j + 1]:
                    self._elems[j], self._elems[j + 1] = self._elems[j + 1], self._elems[j]
                    flag = True
            if not flag:
                break

    def get_res(self):
        return self._elems

if __name__ == '__main__':
    test = [1, 5, 8, 2, 9, 26, 98, 34, 101, 76, 34, 26]
    k1 = Bubble(test)
    k1.bubble()
    print(k1.get_res())
