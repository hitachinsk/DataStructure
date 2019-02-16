import stack_list as sl

max_size = 8
def make_board():
    board = []
    for j in range(max_size):
        line = []
        for i in range(max_size):
            line.append(0)
        board.append(line)
    return board


def check(board, x, y):
    #check in column
    for i in range(max_size):
        if board[i][y] == 1:
            #print('cycgay1')
            return False
    #检查左上斜线
    for i in range(max_size):
        new_x = x - i
        new_y = y - i
        if new_x >= 0 and new_y >= 0 and board[new_x][new_y] == 1:
            #print('cycgay2')
            return False
    #左下斜线
    for i in range(max_size):
        new_x = x + i
        new_y = y - i
        if new_x < max_size and new_y >= 0 and board[new_x][new_y] == 1:
            #print('cycgay3')
            return False
    #右上斜线
    for i in range(max_size):
        new_x = x - i
        new_y = y + i
        if new_x >= 0 and new_y < max_size and board[new_x][new_y] == 1:
            #print('cycgay4')
            return False
    #右下斜线
    for i in range(max_size):
        new_x = x + i
        new_y = y + i
        if new_x < max_size and new_y < max_size and board[new_x][new_y] == 1:
            #print('cycgay5')
            return False
    return True

def dye(board, pos):
    for i in range(max_size):
        board[pos[0]][i] = 0
    board[pos[0]][pos[1]] = 1

def dedye(board, line):
    for i in range(max_size):
        board[line][i] = 0

def print_board(board):
    for each_line in board:
        for each in each_line:
            print(each, end = '')
        print('')

def eight_queen_search(board):
    ss = sl.Stack_list()
    for start_y in range(max_size):
        line = 0
        start = line, start_y
        ss.push(start)
        while not ss.is_empty():
            pos = ss.pop()
            dye(board, pos)
            print_board(board)
            new_line = pos[0] + 1
            if new_line >= max_size:
                print_board(board)
                return True
            for column in range(max_size):
                print(check(board, new_line, column))
                temp = input()
                if check(board, new_line, column):
                    ss.push((pos[0], pos[1] + 1))
                    ss.push((new_line, column))
                    break
            else:
                if pos[1] + 1 == max_size:
                    dedye(board, pos[0])
                else:
                    ss.push((pos[0], pos[1] + 1))
        return False
    


if __name__ == '__main__':
    board = make_board()
    k = eight_queen_search(board)
    print(k)


            
            
            
            
            
            
    
