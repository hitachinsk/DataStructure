import stack_list as sl

def dye(maze, pos):
    maze[pos[0]][pos[1]] = 2

def accessible(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def maze_prob_stack(maze, start, end):
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ss = sl.Stack_list()
    if start == end:
        print(start)
        return True
    else:
        pos = start
        dye(maze, pos)
        ss.push((pos, 0))
        while not ss.is_empty():
            pos, nxt = ss.pop()
            for i in range(nxt, 4):
                nxt_pos = pos[0] + direction[i][0], pos[1] + direction[i][1]
                if nxt_pos == end:
                    ss.push((nxt_pos, i))
                    print_path(ss)
                    return True
                else:
                    if accessible(maze, nxt_pos):
                        ss.push((pos, i + 1))
                        dye(maze, nxt_pos)
                        ss.push((nxt_pos, 0))
                        break
        print('No path found')


def print_path(ss):
    while not ss.is_empty():
        pos = ss.pop()[0]
        print(pos)



if __name__ == '__main__':
    maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
            [1,0,1,0,0,0,0,1,0,1,0,1,0,1],[1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
            [1,0,1,0,0,0,0,0,0,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
            [1,0,1,0,0,0,0,0,0,0,0,1,0,1],[1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
            [1,0,1,0,1,0,1,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
            [1,0,1,0,0,0,1,0,0,1,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    k = maze_prob_stack(maze, (1, 1), (10, 12))
    print(k)
        
