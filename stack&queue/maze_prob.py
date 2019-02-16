#递归方式解决迷宫问题
#0表示可达， 1表示原始迷宫不可达点，2表示由于已经遍历所以不可达点
def dye(maze, pos):
    maze[pos[0]][pos[1]] = 2

def accessible(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def maze_prob(maze, start, end):
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if start == end:
        return True
    else:
        dye(maze, start)
        for i in range(4):
            new_pos = start[0] + direction[i][0],\
                      start[1] + direction[i][1]
            if accessible(maze, new_pos):
                if maze_prob(maze, new_pos, end):
                    print(new_pos)
                    return True
        return False



if __name__ == '__main__':
    maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
            [1,0,1,0,0,0,0,1,0,1,0,1,0,1],[1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
            [1,0,1,0,0,0,0,0,0,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
            [1,0,1,0,0,0,0,0,0,0,0,1,0,1],[1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
            [1,0,1,0,1,0,1,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
            [1,0,1,0,0,0,1,0,0,1,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    k = maze_prob(maze, (1, 1), (10, 12))
    print(k)
        
        
