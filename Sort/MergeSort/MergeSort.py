class MergeSort():
    def __init__(self, elems = []):
        self._elemsfrom = elems

    def ms(self):
        slen, llen = 1, len(self._elemsfrom)
        elemsto = [None] * llen
        while slen < llen:
            self.merge_pass(self._elemsfrom, elemsto, llen, slen)
            slen *= 2
            self.merge_pass(elemsto, self._elemsfrom, llen, slen)
            slen *= 2
        return self._elemsfrom

    def merge(self, lfrom, lto, low, mid, high):
        i, j = low, mid
        counter = low
        while i < mid and j < high:
            if lfrom[i] <= lfrom[j]:
                temp = lfrom[i]
                i += 1
            else:
                temp = lfrom[j]
                j += 1
            lto[counter] = temp
            counter += 1
        while i < mid:
            lto[counter] = lfrom[i]
            i += 1
            counter += 1
        while j < high:
            lto[counter] = lfrom[j]
            j += 1
            counter += 1

    def merge_pass(self, lfrom, lto, llen, slen):
        i = 0
        while i + 2 * slen < llen:
            self.merge(lfrom, lto, i, i + slen, i + 2 * slen)
            i = i + 2 * slen
        if i + slen < llen:
            self.merge(lfrom, lto, i, i + slen, llen)
        else:
            while i < llen:
                lto[i] = lfrom[i]
                i += 1

if __name__ == '__main__':
    test = [1, 5, 8, 2, 9, 26, 98, 34, 101, 76, 34, 26]
    k1 = MergeSort(test)
    print(k1.ms())

