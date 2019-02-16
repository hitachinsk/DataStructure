#smallN problem's solution(using heap)
#find 50 smallest nums in 1000 nums(for simplification)
#get max nums using small-top heap, while get min nums using big-top heap
import random as r
N = 50

def build_heap(heap):
    end = len(heap)
    for i in range(end // 2, -1, -1):
        sift_down(heap, heap[i], i, end)


def sift_down(lis, e, start, end):
    i, j = start, 2 * start + 1
    while j < end:
        if j + 1 < end and lis[j] < lis[j + 1]:
            j += 1
        if e > lis[j]:
            break
        lis[i] = lis[j]
        i = j
        j = 2 * i + 1
    lis[i] = e
    
def dequeue(lis):
    e = lis[-1]
    lis[0] = e
    lis.pop()
    end = len(lis)
    sift_down(lis, lis[0], 0, end)

def enqueue(lis, elem):
    lis.append(elem)
    sift_up(lis, elem)

def sift_up(lis, elem):
    lenth = len(lis)
    i = lenth - 1
    j = (i - 1) // 2
    while i > 0:
        if elem > lis[j]:
            lis[i] = lis[j]
            i = j
            j = (i - 1) // 2
        else:
            break
    lis[i] = elem

def smallN(elems = []):
    heap = []
    for i in range(N):
        heap.append(elems[i])
    build_heap(heap)
    length = len(elems)
    for j in range(N, length):
        if elems[j] >= heap[0]:
            continue
        else:
            dequeue(heap)
            enqueue(heap, elems[j])
    for each in heap:
        print(each)


if __name__ == '__main__':
    test = []
    for i in range(1000):
        test.append(r.randint(10, 10000))
    smallN(test)
