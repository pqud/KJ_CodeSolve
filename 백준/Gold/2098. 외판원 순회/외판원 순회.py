N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [[INF] * (1 << N) for _ in range(N)]

# 시작: 0번 도시부터, 방문 상태는 1 << 0
dp[0][1 << 0] = 0

for visited in range(1 << N):
    for cur in range(N):
        if not (visited & (1 << cur)):
            continue
        for next in range(N):
            if visited & (1 << next):  # 이미 방문했으면 skip
                continue
            if W[cur][next] == 0:  # 경로 없음
                continue
            next_visited = visited | (1 << next)
            dp[next][next_visited] = min(
                dp[next][next_visited],
                dp[cur][visited] + W[cur][next]
            )

# 마지막: 모든 도시를 방문하고 다시 시작점(0)으로 돌아오는 최소 비용
min_cost = INF
for i in range(1, N):
    if W[i][0] == 0:
        continue
    min_cost = min(min_cost, dp[i][(1 << N) - 1] + W[i][0])

print(min_cost)
