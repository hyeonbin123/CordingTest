def solve(db_state, N, W, enemies):
    # dp 테이블 초기화. 4가지 상태를 갖고, 각 상태는 N+1의 길이를 갖습니다.
    dp = [[2 * N] * (N + 1) for _ in range(4)]
    dp[db_state][-1] = 0  # 선택된 상태의 마지막 구역을 0으로 초기화

    for index in range(N):
        for state in range(4):
            # 각 상태에 따라 이전 구역에서의 최소 소대 수를 현재 구역에 적용
            dp[0][index] = min(dp[0][index], dp[state][index - 1] + int(state & 1 == 0) + int(state & 2 == 0))
            # 현재 구역과 위쪽 구역 모두를 커버할 수 있는 경우를 확인
            if enemies[0][index] + enemies[1][index] <= W:
                dp[0][index] = min(dp[0][index], dp[0][index - 1] + 1)
            # 현재 구역과 다음 구역(왼쪽 반대)을 커버할 수 있는 경우를 확인
            if index < N - 1 and enemies[0][index] + enemies[0][index + 1] <= W:
                dp[1][index] = min(dp[1][index], dp[0][index - 1] + 2, dp[2][index - 1] + 1)
            # 현재 구역과 다음 구역(두 번째 행)을 커버할 수 있는 경우를 확인
            if index < N - 1 and enemies[1][index] + enemies[1][index + 1] <= W:
                dp[2][index] = min(dp[2][index], dp[0][index - 1] + 2, dp[1][index - 1] + 1)
            # 두 행의 현재 구역과 다음 구역을 모두 커버할 수 있는 경우를 확인
            if index < N - 1 and enemies[0][index] + enemies[0][index + 1] <= W and enemies[1][index] + enemies[1][index + 1] <= W:
                dp[3][index] = dp[0][index - 1] + 2

    return dp

def solution(N, W, enemies1, enemies2):
    enemies = [enemies1, enemies2]
    result = solve(0, N, W, enemies)[0][N - 1]  # 기본 상태에서 최소 소대 수 계산

    # 첫 번째와 마지막 구역이 함께 커버 가능한 경우의 최소 소대 수 계산
    if enemies[0][0] + enemies[0][N - 1] <= W:
        dp_temp = solve(1, N, W, enemies)
        result = min(result, dp_temp[2][N - 2] + 1, dp_temp[0][N - 2] + 2)
    if enemies[1][0] + enemies[1][N - 1] <= W:
        dp_temp = solve(2, N, W, enemies)
        result = min(result, dp_temp[1][N - 2] + 1, dp_temp[0][N - 2] + 2)
    if enemies[0][0] + enemies[0][N - 1] <= W and enemies[1][0] + enemies[1][N - 1] <= W:
        result = min(result, solve(3, N, W, enemies)[0][N - 2] + 2)

    return result

def main():
    T = int(input())
    for _ in range(T):
        N, W = map(int, input().split())
        enemies1 = list(map(int, input().split()))
        enemies2 = list(map(int, input().split()))
        print(solution(N, W, enemies1, enemies2))

if __name__ == "__main__":
    main()