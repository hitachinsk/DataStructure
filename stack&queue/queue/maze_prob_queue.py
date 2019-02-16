import link_queue as lq

def dye(maze, pos):
    maze[pos[0]][pos[1]] = 2

def accessible(maze, pos):
    return maze[pos[0]][pos[1]] == 0

def maze_prob_queue(maze, start, end):
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ss = lq.Linkqueue()
    if start == end:
        print(start)
        return True
    else:
        dye(maze, start)
        ss.enqueue(start)
        while not ss.is_empty():
            pos = ss.dequeue()
            for i in range(4):
                new_pos = pos[0] + direction[i][0], pos[1] + direction[i][1]
                if accessible(maze, new_pos):
                    if new_pos == end:
                        print('Path found')
                        return True
                    else:
                        ss.enqueue(new_pos)
                        dye(maze, new_pos)
        print('Path not found')


if __name__ == '__main__':
    maze = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
            [1,0,1,0,0,0,0,1,0,1,0,1,0,1],[1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
            [1,0,1,0,0,0,0,0,0,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
            [1,0,1,0,0,0,0,0,0,0,0,1,0,1],[1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
            [1,0,1,0,1,0,1,0,1,0,1,0,0,1],[1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
            [1,0,1,0,0,0,1,0,0,1,0,0,0,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    k = maze_prob_queue(maze, (1, 1), (10, 12))
    print(k)
