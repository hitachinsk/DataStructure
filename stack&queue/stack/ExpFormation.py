import stack_list as sl
class EStack_list(sl.Stack_list):
    def depth(self):
        return len(self._elem)

#将字符串按照项数变为列表
def str2int_inlis(lis):
    len_ = len(lis)
    for i in range(len_):
        if lis[i].isdigit() == True:
            lis[i] = int(lis[i])
    return lis


#后缀表达式计算得到结果
def calc_lis(lis):
    op = str2int_inlis(lis)
    print(op)
    k1 = EStack_list()
    operator = '+-*/'
    for each in op:
        if str(each) in operator:
            if k1.depth() <= 1:
                raise SyntaxError('operstor cannot calc with no more than 2 depth.')
            else:
                s1 = k1.pop()
                s2 = k1.pop()
                if each == '+':
                    c = s1 + s2
                elif each == '-':
                    c = s2 - s1
                elif each == '*':
                    c = s1 * s2
                else:
                    if s1 == 0:
                        raise ZeroDivisionError
                    else:
                        c = s2 / s1
                k1.push(c)
        elif str(each) not in operator:
            k1.push(each)
        else:
            break
    if k1.depth() == 1:
        return k1.top()
    else:
        raise SyntaxError('cannot get a uniform result')

#中缀表达式变为后缀表达式
def mid2post(line):
    res = []
    ss = EStack_list()
    operator = '+-*/()'
    degree = {'(':1, ')':1, '*':3, '/':3, '+':5, '-':5}

    for x in tokens(line):
        if x not in operator:
            res.append(x)
        else:
            if ss.is_empty() or x == '(':
                ss.push(x)
            elif x == ')':
                while (not ss.is_empty()) and ss.top() != '(':
                    res.append(ss.pop())
                if ss.is_empty() == True:
                    raise SyntaxError('parens cannot match each other')
                ss.pop()
            else:
                while (not ss.is_empty()) and (degree[ss.top()] >= degree[x]):
                    res.append(ss.pop())
                ss.push(x)

    while not ss.is_empty():
        if ss.top == '(':
            raise SyntaxError('parens cannot clear')
        else:
            res.append(ss.pop())

    return res

#生成器token的制作,这里默认每一个小数后面都会有一个空格做结尾
def tokens(line):
    i, length = 0, len(line)
    operator = '+-*/()'
    while i < length:
        while line[i].isspace():
            i += 1
        if i >= length:
            break
        if line[i] in operator:
            yield line[i]
            i += 1
            continue

        j = i + 1
        while (not line[j].isspace()) and (j < length) and \
              (line[j] not in operator):
            if (line[j] == 'e' or line[j] == 'E') and line[j + 1] == '-'\
               and j+1 < length:
                print('cyc')
                j += 1
            j += 1
        yield line[i:j]
        i = j
            
        
                    
if __name__ == '__main__':
    text = '(3+2)*4*5/(2+7)'
    k = mid2post(text)
    s = calc_lis(k)
    print(s)
    
            
