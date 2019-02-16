#数字大了之后复杂度非常高
#这里采用m进出栈而变化n的方式来进行函数非递归的实现
#但是毫无疑问，Ackerman函数用递归实现虽然牺牲部分效率，但是代码十分简洁
import stack_list as sl

def Ack_stack(m, n):
    ss = sl.Stack_list()
    ss.push(m)
    while not ss.is_empty():
        m = ss.pop()
        if m == 0:
            n = n + 1
        elif n == 0:
            n = 1
            ss.push(m - 1)
        else:
            n = n - 1
            ss.push(m - 1)
            ss.push(m)
    return n


k = Ack_stack(3, 2)

print(k)        
    
