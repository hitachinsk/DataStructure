import KMP

def tokens(string, seps):
    seq = KMP.KMP_main(string, seps)
    sl = len(string)
    spl = len(seps)
    seql = len(seq)
    max_len = 0
    max_former = 0
    former = 0
    for i in range(seql):
        new_max = seq[i] - former
        if new_max > max_len:
            max_len = new_max
            max_former = former
        former = seq[i] + spl
    new_max = sl - former
    if new_max > max_len:
        max_len = new_max
        max_former = former
    for j in range(max_former, max_former + max_len):
        yield string[j]


m = tokens('asdfghjklasdpoasdiasdjnb', 'asd')
for each in m:
    print(each)
