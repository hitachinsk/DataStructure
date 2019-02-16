import LLClass as LC

k1 = LC.LList()
op = [1,2,3,4,5]
k1.list2linklist(op)
k1.printall()
k1.del_minimal()
k1.del_if(lambda y:y % 2 == 0)
len(k1)
print(k1.linklist2list())
k1.printall()
k2 = LC.LList()

for i in range(10):
    k1.prepend(i)
    k2.prepend(i+1)

print(k2 > k1)

for i in range(11, 20):
    k1.append(i)
k1.printall()
print(len(k1))

k1.reverse()
k1.printall()
print('')
print('cyc')
k1.sort()
k1.printall()

