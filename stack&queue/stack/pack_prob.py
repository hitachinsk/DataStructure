#0-1 package problem,given sum of weight and weight of all the items.
#But there is only one item for each kind.
#weight:sum of weight, wlist:a list contains the weight of all items, n:num of items that are picked
def pack_prob(weight, wlist, n):
    if weight == 0:
        return True
    if (weight < 0) or (weight > 0 and n < 1):
        return False
    if pack_prob(weight, wlist, n-1):
        return True
    if pack_prob(weight-wlist[n-1], wlist, n-1):
        print('Item ' + str(n) + ' weights ' + str(wlist[n-1]) + ' has been picked')
        return True
    else:
        return False



if __name__ == '__main__':
    wlist = [3, 5, 10, 17, 20, 25]
    weight = 45
    n = 6
    m = pack_prob(weight, wlist, n)
    print(m)
