def solve(n, board):
    # 검은 칸과 흰 칸을 분리
    black = [(i, j) for i in range(n) for j in range(n) if (i+j) % 2 == 0 and board[i][j] == 1]
    white = [(i, j) for i in range(n) for j in range(n) if (i+j) % 2 == 1 and board[i][j] == 1]

    def is_safe(pos, bishops):
        for bishop in bishops:
            if abs(pos[0] - bishop[0]) == abs(pos[1] - bishop[1]):
                return False
        return True

    def backtrack(candidates, bishops):
        if not candidates:
            return len(bishops)
        
        pos = candidates.pop()
        max_bishops = backtrack(candidates, bishops)
        
        if is_safe(pos, bishops):
            bishops.append(pos)
            max_bishops = max(max_bishops, backtrack(candidates, bishops))
            bishops.pop()
        
        candidates.append(pos)
        return max_bishops

    return backtrack(black, []) + backtrack(white, [])

# 입력 받기
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(solve(n, board))