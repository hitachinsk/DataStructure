class Bubble_doubleway():
    def __init__(self, elems):
        self._elems = elems

    def bubble_doubleway(self):
        counter = 1
        start, end = 0, len(self._elems)
        while counter < len(self._elems):
            flag = True
            if counter % 2 == 1:
                for i in range(start, end):
                    if i + 1 < end and self._elems[i] > self._elems[i + 1]:
                        self._elems[i], self._elems[i + 1] = self._elems[i + 1], self._elems[i]
                        flag = False
                end -= 1
            else:
                i = end - 1
                while i > start:
                    if self._elems[i] < self._elems[i - 1]:
                        self._elems[i], self._elems[i - 1] = self._elems[i - 1], self._elems[i]
                        flag = False
                    i -= 1
                start += 1
            if flag:
                break
            counter += 1

    def get_res(self):
        return self._elems

if __name__ == '__main__':
    test = [1, 5, 8, 2, 9, 26, 98, 34, 101, 76, 34, 26]
    k1 = Bubble_doubleway(test)
    k1.bubble_doubleway()
    print(k1.get_res())

