import KMP
def string_replace(text, pattern, repl):
    temp = []
    former = 0
    k = KMP.KMP_main(text, pattern)
    pl = len(pattern)
    rl = len(repl)
    for each in k:
        temp.append(text[former : each])
        temp.append(text[each : each + pl])
        former = each + pl
    temp.append(text[former : ])
    mp = len(temp)
    for i in range(mp):
        if temp[i] == pattern:
            temp[i] = repl
    res = ''
    for j in range(mp):
        res += temp[j]
    return res


kf = string_replace('asdfghjklasdfghjklasdfghjkl', 'asd', 'qwe')
print(kf)
