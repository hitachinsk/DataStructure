#时间复杂度(O(m+n))
def ssc(list1, list2):
    res = []
    m, n = len(list1), len(list2)
    i = j = 0
    while i < m and j < n:
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    if i >= m:
        while j < n:
            res.append(list2[j])
            j += 1
    elif j >= n:
        while i < m:
            res.append(list1[i])
            i += 1

    return res


list1 = [1,3,5,7,9, 12, 14, 19]
list2 = [2,4,6,7, 8, 9 ,10]

kd = ssc(list1, list2)
print(kd)
