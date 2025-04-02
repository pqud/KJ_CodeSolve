import sys
from collections import deque
input = sys.stdin.readline


dx,dy = [-1, 1, 0, 0],[0, 0, -1, 1]
year = 0
ice = []



def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    seaList = []

    while queue:
        cx, cy = queue.popleft()
        sea = 0
        for i in range(4):
            nx,ny = cx + dx[i],cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

        if sea > 0: #물 차오른건 한번에 처리를 해야함함
            seaList.append((cx, cy, sea))
    for cx, cy, sea in seaList:
        graph[cx][cy] = max(0, graph[cx][cy] - sea)

    return 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))


while ice:
    visited = [[0] * m for _ in range(n)]
    delList = []
    group = 0

    for i, j in ice: #빙하 기준으로 시작 
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j) #빙하 녹이기 
        if graph[i][j] == 0:
            delList.append((i, j)) #제거 리스트에 담음
    if group > 1: #그룹 개수가 1개 이상이면 
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList))) #ice 리스트에서 delList에 있는 것들 제거거
    year += 1

if group < 2:
    print(0)
