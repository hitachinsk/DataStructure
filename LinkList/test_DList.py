import DList as DL

test1 = DL.DList()

print(test1.isEmpty())
for i in range(10):
    test1.prepand(i)

for i in range(11, 20):
    test1.append(i)

k = test1.find(lambda y:y % 2 == 0)

for each in k:
    print(each)
    
test1.pop()
test1.pop_last()
test1.printall()
