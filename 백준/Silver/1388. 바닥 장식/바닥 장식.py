import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

def dfs(x, y, tile):
    visited[x][y] = True

    if tile == '-':
        if y+1 < M and not visited[x][y+1] and graph[x][y+1] == '-':
            dfs(x, y+1, tile)
    elif tile == '|':
        if x+1 < N and not visited[x+1][y] and graph[x+1][y] == '|':
            dfs(x+1, y, tile)

answer = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            answer += 1

print(answer)
