import copy

def move(board, direction):
    N = len(board)
    new_board = [row[:] for row in board]
    
    if direction in ['left', 'right']:
        for i in range(N):
            new_board[i] = move_line(new_board[i], direction == 'right')
    else: 
        for j in range(N):
            column = [new_board[i][j] for i in range(N)]
            column = move_line(column, direction == 'down')
            for i in range(N):
                new_board[i][j] = column[i]
    
    return new_board

def move_line(line, reverse):
    N = len(line)
    if reverse:
        line = line[::-1]
    
    new_line = []
    merged = False
    for num in line:
        if num == 0:
            continue
        if new_line and new_line[-1] == num and not merged:
            new_line[-1] *= 2
            merged = True
        else:
            new_line.append(num)
            merged = False
    
    new_line += [0] * (N - len(new_line))
    
    if reverse:
        new_line = new_line[::-1]
    
    return new_line

def get_max_value(board):
    return max(max(row) for row in board)

def backtrack(board, depth):
    if depth == 5:
        return get_max_value(board)
    
    max_value = get_max_value(board)
    for direction in ['up', 'down', 'left', 'right']:
        new_board = move(board, direction)
        if new_board != board:
            max_value = max(max_value, backtrack(new_board, depth + 1))
    
    return max_value

def solve_2048(board):
    return backtrack(board, 0)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(solve_2048(board))