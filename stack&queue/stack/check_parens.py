import stack_list as sl

def check_parens(text):
    open_parens = '([{\'\"#'
    parens = '()[]{}\'\"#\n'
    parens_match = {')':'(', ']':'[', '}':'{', '\'':'\'', '\"':'\"', '\n':'#'}
    spb = '\'\"#\n'

    def parens_generator(text):
        i, length = 0, len(text)
        while True:
            while i < length and text[i] not in parens:
                i += 1
            if i >= length:
                return
            else:
                yield text[i], i
                i += 1

    stack = sl.Stack_list()
    for pas, index in parens_generator(text):
        temp = input()
        if pas in open_parens:
            if stack.is_empty():
                stack.push(pas)
            else:
                if stack.top() == '\'' or stack.top() == '\"':
                    if pas == stack.top():
                        stack.pop()
                        continue
                if stack.top() not in spb:
                    stack.push(pas)
        else:
            if stack.is_empty():
                print('The text begins with a close paren')
                return False
            if stack.top() in spb:
                if pas not in spb:
                    continue
            if parens_match[pas] == stack.top():
                stack.pop()
            else:
                print('Thw parens in the text cannot match in ' + str(index))
                return False
        stack.print_stack()
    if stack.is_empty():
        return True
    else:
        return False


text = '#dewqd()[]{}(\n\'(\'23+9[iop{pol}])'
k = check_parens(text)
print(k)
