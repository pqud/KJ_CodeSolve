import sys

input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = 1  # 시작점에서의 경로 수는 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:  # 도착점에 도달하면 더 이상 진행하지 않음
            break
        if dp[i][j] != 0:  # 현재 위치로 올 수 있는 경로가 존재할 때만 진행
            value = table[i][j]
            nx = j + value
            ny = i + value
            if nx < n:  # 오른쪽으로 이동
                dp[i][nx] += dp[i][j]
            if ny < n:  # 아래로 이동
                dp[ny][j] += dp[i][j]

print(dp[n - 1][n - 1])  # 도착점에서의 경로 수 출력
