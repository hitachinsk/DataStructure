class Verror(ValueError):
    pass

class Lnode():
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_


class LList():
    def __init__(self):
        self._head = None
        self._rear = None
        self._length = 0

    def isEmpty(self):
        return self._head is None

    def deleteLink(self):
        self._head = None
        self._rear = None
        self._length = 0

    def prepend(self, elem):
        self._head = Lnode(elem, self._head)
        self._length += 1

    def pop(self):
        if self._head is None:
            raise Verror('pop a null link')
        if self._head.next == None:
            e = self._head.elem
            self._head = None
        else:
            e = self._head.elem
            self._head = self._head.next
        
        self._length -= 1
        return e

    def append(self, elem):
        if self._head is None:
            self._head = Lnode(elem)
            self._rear = self._head
        else:
            p = self._head
            while p.next:
                p = p.next
            p.next = Lnode(elem)
            self._rear = p.next

        self._length += 1

    def pop_last(self):
        if not self._head:
            raise Verror('pop_last utilities in a null link')
        p = self._head
        if not p.next:
            e = p.elem
            self._head = None
            self._rear = None
        else:
            while p.next.next:
                p = p.next
            e = p.next.elem
            p.next = None
            self._rear = p

        self._length -= 1
        return e

    def find(self, pred):
        p = self._head
        while p:
            if pred(p.elem):
                yield p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p:
            print(p.elem, end = '')
            if p.next:
                print(',', end = '')
            p = p.next
        print('')

    def insert(self, loc, elem):
        p = self._head
        if not loc:
            self._head = Lnode(elem, self._head.next)
        else:
            k = loc - 1
            while p and k > 0:
                p = p.next
                k -= 1
            if k > 0:
                raise Verror('insert flow')
            else:
                p.next = Lnode(elem, p.next)

        self._length += 1

    def pop_pt(self, loc):
        p = self._head
        if not p:
            raise Verror('pop_pt utilities in a null link')
        else:
            if not loc:
                e = self._head.elem
                self._head = self._head.next
            else:
                k = loc - 1
                while p and k > 0:
                    p = p.next
                    k -= 1
                if k > 0:
                    raise Verror('location out of range')
                else:
                    e = p.next.elem
                    p.next = p.next.next

            self._length -= 1
            return e

    def remove(self, elem):
        p = self._head
        if not p:
            return
        if p.elem == elem:
            self._head = self._head.next
        else:
            while p.next and p.next.elem != elem:
                p = p.next
            if p.next == None:
                raise Verror('can\'t find the elem')
            if p.next.elem == elem:
                p.next = p.next.next

        self._length -= 1

    def __len__(self):
        return self._length

    def __eq__(self, another):
        p, q = self._head, another._head
        while p and q and p.elem == q.elem:
            p = p.next
            q = q.next
        if not(p or q):
            return True
        else:
            return False

    def __lt__(self, another):
        p, q = self._head, another._head
        while p and q and p.elem < q.elem:
            p = p.next
            q = q.next
        if not(p or q):
            return True
        else:
            return False

    def __gt__(self, another):
        p, q = self._head, another._head
        while p and q and p.elem > q.elem:
            p = p.next
            q = q.next
        if not(p or q):
            return True
        else:
            return False

    def reverse(self):
        q = None
        while self._head:
            p = self._head
            self._head = self._head.next
            p.next = q
            q = p
        self._head = q
            

    def sort(self):
        p = self._head
        if (not p) or (not p.next):
            return
        else:
            rem = p.next
            p.next = None
            while rem:
                p = self._head
                q = None
                while p and p.elem <= rem.elem:
                    q = p
                    p = p.next
                if not q:
                    self._head = rem
                else:
                    q.next = rem
                q = rem
                rem = rem.next
                q.next = p
                    
    def max_elem(self):
        if not self._head:
            raise TypeError
        else:
            p = self._head
            max_fac = p.elem
            while p:
                if p.elem > max_fac:
                    max_fac = p.elem
                p = p.next
            return max_fac
        
    def min_elem(self):
        if not self._head:
            raise TypeError
        else:
            p = self._head
            min_fac = p.elem
            while p:
                if p.elem < min_fac:
                    min_fac = p.elem
                p = p.next
            return min_fac

    def del_minimal(self):
        minimal = self.min_elem()
        self.remove(minimal)

    def del_if(self, pred):
        p = self._head
        if not p:
            return
        if not p.next:
            if pred(p.elem):
                self._head = None
                self._length -= 1
            return
        while p.next:
            if pred(p.next.elem):
                if p.next.next == None:
                    p.next = None
                else:
                    p.next = p.next.next
                self._length -= 1
            else:
                p = p.next
        if pred(self._head.elem):
            p = self._head
            self._head = self._head.next
            p.next = None
            self._length -= 1

    def del_duplicate(self):
        lis = []
        p = self._head
        lis.append(p.elem)
        if (not p) or (not p.next):
            return
        while p.next:
            if p.next.elem not in lis:
                lis.append(p.next.elem)
                p = p.next
            else:
                if p.next.next == None:
                    p.next = None
                else:
                    p.next = p.next.next
                self._length -= 1

    def interleaving(self, another):
        length = min((len(self), len(another)))
        print(length)
        p = self._head
        q = another._head
        for i in range(length - 1):
            m = p.next
            n = q.next
            p.next = q
            p = p.next
            p.next = m
            p = p.next
            q = n
        if q:
            p.next = q

    def enumerate(self):
        p = self._head
        if p:
            index = 0
            while p:
                print('index = ' + str(index) + ', value = ' + str(p.elem))
                index += 1
                p = p.next

    def list2linklist(self, lis):
        self.deleteLink()
        length = len(lis)
        for i in range(length):
            self.append(lis[i])

    def linklist2list(self):
        lis = []
        p = self._head
        while p:
            lis.append(p.elem)
            p = p.next
        return lis

    def rev_visit(self, op):
        self.reverse()
        p = self._head
        while p:
            op(p.elem)
            print(p.elem)
            p = p.next
        self.reverse()

    def get_head(self):
        return self._head

    def modify(self, pointer):
        self._head = pointer

    

def partition(lst, pred):
    k2 = LList()
    p = lst.get_head()
    if not p or not p.next:
        return
    else:
        while p and p.next:
            if not pred(p.next.elem):
                k2.append(p.next.elem)
                k2.printall()
                p.next = p.next.next
            p = p.next

        if not pred(lst._head.elem):
            k2.prepend(lst.get_head().elem)
            p = lst.get_head()
            lst.modify(p.next)
        return lst, k2
        
