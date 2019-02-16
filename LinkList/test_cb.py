import LLClass as LC

lst1 = LC.LList()
lst2 = LC.LList()

for i in range(10):
    lst1.append(i)
    lst2.append(i+1)
for i in range(10):
    lst1.append(i)

lst1.printall()
print('cyc1')
lst1.del_duplicate()
lst1.printall()
print('cyc2')
lst1.del_if(lambda y:y % 2 == 0)
lst1.printall()

