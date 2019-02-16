def eight_quene():
    for i in range(8):
        res = [i]
        for j in range(1, 8):
            for m in range(8):
                if (m not in res) and not_in_crossline(m, res):
                    res.append(m)
        print(res)



def not_in_crossline(index, lis):
    length = len(lis)
    flag = True
    for i in range(length):
        if abs(i - length) == abs(lis[i] - index):
            flag = False
            break
    if flag:
        return True
    else:
        return False


eight_quene()
