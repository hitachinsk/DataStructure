class CounterSort():
    def __init__(self, elems = []):
        self._elems = elems
        maxk, mink = self._findmaxmin()
        self._max = maxk
        self._min = mink

    def _findmaxmin(self):
        maxk = mink = self._elems[0]
        for each in self._elems:
            if each > maxk:
                maxk = each
            if each < mink:
                mink = each
        return maxk, mink

    def countersort(self):
        for each in self._elems:
            if not isinstance(each, int):
                raise ValueError('CounterSort must be applied to int type')
        llen = len(self._elems)
        temp = [0] * (self._max - self._min + 1)
        for each in self._elems:
            temp[each - self._min] += 1
        counter = 0
        for i in range(len(temp)):
            k = temp[i]
            while k > 0:
                self._elems[counter] = self._min + i
                counter += 1
                k -= 1
        return self._elems

    def bucketsort(self):
        flag = False
        for each in self._elems:
            if isinstance(each, float):
                flag = True
        if not flag:
            raise ValueError('At least one float elem should be in the list if you wanna use bucketsort')
        bucket_num = int(self._max - self._min) + 1
        res = [[] for i in range(bucket_num)]
        for each in self._elems:
            res[int(each - self._min)].append(each)
        for i in range(bucket_num):
            res[i] = self._insertionsort(res[i])
        counter = 0
        for a in res:
            for b in a:
                self._elems[counter] = b
                counter += 1
        return self._elems

    def _insertionsort(self, lis):
        op = list(lis)
        for i in range(1, len(op)):
            x = op[i]
            j = i
            while j > 0:
                j -= 1
                if x < op[j]:
                    op[j + 1] = op[j]
                else:
                    j += 1
                    break
            lis[j] = x
        return op


if __name__ == '__main__':
    test = [1.5, 2.5, 4.8, 3.2, 1.9, 2.6, 3.8, 6.4, 5.1, 4.6, 2.4, 7.6]
    k1 = CounterSort(test)
    print(k1.bucketsort())