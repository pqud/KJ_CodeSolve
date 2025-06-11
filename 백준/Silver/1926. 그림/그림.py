import sys
input = sys.stdin.readline

dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

n, m = map(int, input().split())
visited = [[False]*m for _ in range(n)]
graph = []
cnt = 0
largest = 0

def dfs(y, x):
    stack = [(y, x)]
    visited[y][x] = True
    area = 0
    while stack:
        cy, cx = stack.pop()
        area += 1
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    stack.append((ny, nx))
    return area

for _ in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            largest = max(largest, dfs(i, j))
            cnt += 1

print(cnt)
print(largest)
