def count_board(board,y,x):
    count1,count2=0,0
    for i in range(8):
        for j in range(8):
            if (i+j)%2==0:
                if board[y+i][x+j] != 'W':
                    count1+=1
                if board[y+i][x+j] != 'B':
                    count2+=1
            else:
                if board[y+i][x+j] != 'W':
                    count2+=1
                if board[y+i][x+j] != 'B':
                    count1+=1
    return min(count1,count2)

def solve_board(n,m,board):
    min_count=float('inf')
    for y in range(n-7):
        for x in range(m-7):
            min_count=min(min_count,count_board(board,y,x))
    return min_count

def main():
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    result = solve_board(N,M,board)
    print(result)

if __name__ == "__main__":
    main()