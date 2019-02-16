class LNode():
    def __init__(self, char, next_ = None):
        self.elem = char
        self.next = next_


class Link_Str():
    def __init__(self, string = None):
        self._length = 0
        if string:
            sl = len(string)
            self._head = LNode(string[0])
            p = self._head
            for i in range(1, sl):
                p.next = LNode(string[i])
                p = p.next
            self._length += len(string)
        else:
            self._head = None

    def printall(self):
        p = self._head
        while p:
            print(p.elem, end = '')
            p = p.next
        print('')

    def __len__(self):
        return self._length

    def replace(self, target, repl):
        p = self._head
        kls = self.naive_match(target)
        if not kls:
            return
        counter = 0
        while p:
            if counter == kls[0] - 1:
                h1 = p
            if counter == kls[0] + len(target):
                h2 = p
                break
            p = p.next
            counter += 1
        h1.next = repl._head
        m = repl._head
        while m.next:
            m = m.next
        m.next = h2

    def naive_match(self, pattern):
        p = self._head
        sto = p
        h = pattern._head
        res = []
        counter = 0
        counter_head = 0
        while p:
            if p.elem == h.elem:
                if not h.next:
                    print(counter)
                    res.append(counter - len(pattern) + 1)
                    p = sto.next
                    h = pattern._head
                    sto = p
                    counter_head += 1
                    counter = counter_head
                    continue
                else:
                    p = p.next
                    h = h.next
                    counter += 1
            if p.elem != h.elem:
                p = sto.next
                h = pattern._head
                sto = p
                counter_head += 1
                counter = counter_head
        return res

    def pnextok(self, pattern):
        i, k, m = 0, -1, len(pattern)
        p_k = pattern._head
        p_i = pattern._head
        pnext = [-1] * m
        if k > 0:
            p_k = pattern._head
            for s in range(k):
                p_k = p_k.next
        if i > 0:
            p_i = pattern._head
            for s in range(i):
                p_i = p_i.next
        while i < m-1:
            if k == -1 or p_i == p_k:
                i, k = i + 1, k + 1
                if p_i == p_k:
                    pnext[i] = pnext[k]
                else:
                    pnext[i] = k
            else:
                k = pnext[k]
                
            if k > 0:
                p_k = pattern._head
                for s in range(k):
                    p_k = p_k.next
            if i > 0:
                p_i = pattern._head
                for s in range(i):
                    p_i = p_i.next
        return pnext
                
    def KMP_match(self, pattern):
        t = self._head
        p = pattern._head
        j, i = 0, 0
        n, m = len(self), len(pattern)
        pnext = self.pnextok(pattern)
        while t and p:
            if i == -1 or t.elem == p.elem:
                t = t.next
                p = p.next
                j, i = j+1, i+1
            else:
                i = pnext[i]
                if i != -1:
                    p = pattern._head
                    for m in range(i):
                        p = p.next
        if not p:
            return j - i
        return -1

    def find_in(self, another):
        p = self._head
        q = another._head
        flag = False
        counter = 0
        while p:
            q = another._head
            while q:
                if p.elem == q.elem:
                    flag = True
                    break
                else:
                    q = q.next
            if flag == True:
                break
            else:
                p = p.next
                counter += 1
        if flag == True:
            return counter
        else:
            return -1

    def find_not_in(self, another):
        p = self._head
        q = another._head
        counter = 0
        flag = False
        while p:
            q = another._head
            while q:
                if p.elem == q.elem:
                    break
                else:
                    q = q.next
            if not q:
                flag = True
                break
            else:
                p = p.next
                counter += 1
        if flag == True:
            return counter
        else:
            return -1

    def remove(self, another):
        p = self._head
        if (not p) or (not another):
            return
        if not p.next:
            k = another._head
            while k:
                if p.elem == k.elem:
                    break
                else:
                    k = k.next
            if k:
                self._head = None
            else:
                return
        if p.next:
            while p.next:
                k = another._head
                while k:
                    if p.next.elem == k.elem:
                        break
                    else:
                        k = k.next
                if k:
                    if p.next.next:
                        p.next = p.next.next
                    else:
                        p.next = None
                else:
                    p = p.next
            p = self._head
            k = another._head
            while k:
                if p.elem == k.elem:
                    break
                else:
                    k = k.next
            if k:
                self._head = self._head.next
            else:
                return
                
        
        
                

k1 = Link_Str('asdfghjklfghkiofgh')
k2 = Link_Str('fgh')
k3 = Link_Str('gen.g')
k4 = Link_Str('asdfghiko')
k1.printall()
m = k1.KMP_match(k2)
print(m)
#m = len(k1)
#print(m)
#k1.replace(k2, k3)
#k1.printall()
s = k1.find_in(k3)
print(s)
h = k1.find_not_in(k4)
print(h)
k1.remove(k2)
k1.printall()
