#retain some common hash functions
class HashFunc():
    def __init__(self, elem=None):
        """

        :type elem: list
        """
        if elem is None:
            elem = []
        else:
            for each in elem:
                if not isinstance(each, int):
                    raise ValueError('Not all of factors in elem are integer')
        self._elem = elem
        self._length = None
        self._div = None
        self._doublediv = None
        self._flag = None
        self._res = []

    #in de-conflict way
    def div_mod_sequ(self, p, length):
        self._div = p
        self._length = length
        self._flag = 1
        res = [None] * length
        assert p <= length
        for i in range(len(self._elem)):
            index = self._elem[i] % p
            while res[index] is not None:
                index = (index + 1) % length
            res[index] = self._elem[i]
        self._res = res
        return res

    def div_mod_dobule_hash(self, p, length, q):
        self._div = p
        self._length = length
        self._doublediv = q
        self._flag = 2
        res = [None] * length
        assert q < p <= length
        for i in range(len(self._elem)):
            index = self._elem[i] % p
            while res[index] is not None:
                index = (index + (self._elem[i] % q) + 1) % length
            res[index] = self._elem[i]
            self._res = res
        return res

    #outer de-conflict tech:zig tech
    def zig(self, length):
        self._length = length
        self._flag = 3
        res = []
        for i in range(length):
            res.append([])
        for each in self._elem:
            index = each % length
            res[index].append(each)
        self._res = res
        return res

    #search func in Hash type
    def search(self, key):
        if not self._flag:
            raise TypeError('Index has not been hashed')
        if self._flag == 1:
            index = key % self._div
            old_index = index
            while self._res[index] != key:
                index = (index + 1) % self._length
                if self._res[index] == None or index == old_index:
                    print('Key doesn\'t exist in result')
                    return -1
            return index
        elif self._flag == 2:
            index = key % self._div
            old_index = index
            step = key % self._doublediv + 1
            while self._res[index] != key:
                index = (index + step) % self._length
                if self._res[index] == None or index == old_index:
                    print('Key doesn\'t exist in result')
                    return -1
            return index
        else:
            index = key % self._length
            for each in self._res[index]:
                if key == each:
                    return index
            print('Key doesn\'t exist in result')
            return -1

    def delete(self, key):
        index = self.search(key)
        if index != -1:
            if self._flag != 3:
                self._res[index] = -1
            else:
                for i in range(len(self._res[index])):
                    if self._res[index][i] == key:
                        self._res[index][i] = -1

    def insert(self, key):
        if not self._flag:
            raise TypeError('Index has not been hashed')
        if self._flag == 1:
            index = key % self._div
            old_index = index
            while self._res[index] is not None:
                index = (index + 1) % self._length
                if index == old_index:
                    print('The store area is full')
                    return -1
            self._res[index] = key
            return
        elif self._flag == 2:
            index = key % self._div
            old_index = index
            step = key % self._doublediv + 1
            while self._res[index] is not None:
                index = (index + step) % self._length
                if index == old_index:
                    print('The store area is full')
                    return -1
            self._res[index] = key
            return
        else:
            index = key % self._length
            self._res[index].append(key)
            return

    def get_res(self):
        return self._res


if __name__ == '__main__':
    KEY = [18, 73, 10, 5, 68, 99, 22, 32, 46, 58, 25]
    temp = HashFunc(KEY)
    #k = temp.div_mod_sequ(13, 13)
    #s = temp.zig(8)
    t = temp.div_mod_dobule_hash(13, 13, 5)
    #print(k)
    #print(s)
    #print(t)
    temp.delete(99)
    print(temp.get_res())