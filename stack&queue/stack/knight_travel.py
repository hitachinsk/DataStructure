import stack_list as sl

N = 8

def make_board():
    res = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(0)
        res.append(temp)
    return res

def dye(board, pos, lis):
    board[pos[0]][pos[1]] = len(lis) + 1

def accessible(board, pos):
    return board[pos[0]][pos[1]] == 0

def print_board(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = '  ')
        print('\n')

def dedye(board, pos):
    board[pos[0]][pos[1]] = 0

def print_path(board, stack):
    while not stack.is_empty():
        pos = stack.pop()[0]
        if board[pos[0]][pos[1]] != 0:
            print(pos)

#x and y are the start point of knight
#DFS search from direction 1 to 8
def knight_travel(board, x, y):
    path = []
    direction = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    ss = sl.Stack_list()
    pos = (x, y)
    dye(board, pos, path)
    ss.push((pos, 0))
    path.append(pos)
    while not ss.is_empty():
        pos, nxt = ss.pop()
        #print_board(board)
        #temp = input()
        for i in range(nxt, 8):
            new_pos = pos[0] + direction[i][0], pos[1] + direction[i][1]
            if len(path) == N * N:
                print_path(path)
                return True
            if 0 <= new_pos[0] <= 7 and 0 <= new_pos[1] <= 7 and accessible(board, new_pos):
                ss.push((pos, i + 1))
                dye(board, new_pos, path)
                ss.push((new_pos, 0))
                path.append(new_pos)
                break
        else:
            #退染色
            dedye(board, pos)
            #删节点路径
            path.pop()
    print('Cannot find a route')
    return False


if __name__ == '__main__':
    board = make_board()
    k = knight_travel(board, 3, 3)
    print(k)
    
