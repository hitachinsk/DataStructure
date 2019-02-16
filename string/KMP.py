def pnext_solution(p_string):
    length = len(p_string)
    pnext = [-1] * length
    i, k = 0, -1
    while i < length - 1:
        if k == -1 or p_string[i] == p_string[k]:
            i, k = i + 1, k + 1
            pnext[i] = k
        else:
            k = pnext[k]
    print(pnext)

    return pnext


def KMP_main(t_string, p_string):
    pnext = pnext_solution(p_string)
    length = len(t_string)
    length_p = len(p_string)
    res = []
    k = -1
    for i in range(length):
        while k > -1 and t_string[i] != p_string[k+1]:
            k = pnext[k]
        #next match from index k
        if t_string[i] == p_string[k+1]:
            k += 1
        if k == length_p - 1:
            res.append(i - length_p + 1)
            k = -1

    return res


#m = KMP_main('abacabadabacabafabag', 'abac')
#print(m)        
