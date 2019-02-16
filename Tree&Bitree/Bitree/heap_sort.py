#堆排序，对传入的一个列表数据进行排序，最终可达O(nlogn)时间复杂度
#而空间复杂度只为O(1)
#小顶堆得到的排序序列是降序，而大顶堆是升序

def heap_sort(lis):
    op = list(lis)
    end = len(op)
    for i in range(end // 2, -1, -1):
        siftdown(op, op[i], i, end)
    for i in range(end):
        e = op[0]
        op[0] = op[end - 1 - i]
        op[end - 1 - i] = e
        siftdown(op, op[0], 0, end - 1 - i)
    return op


#向下筛选函数，递归构建初始堆，这里构建小顶堆
def siftdown(lis, e, start, end):
    i, j = start, 2 * start + 1
    while j < end:
        if j + 1 < end and lis[j] > lis[j + 1]:
            j += 1
        if e < lis[j]:
            break
        lis[i] = lis[j]
        i = j
        j = 2 * i + 1
    lis[i] = e


if __name__ == '__main__':
    temp = [1,8,4,9,2,7,5]
    k = heap_sort(temp)
    print(k)
