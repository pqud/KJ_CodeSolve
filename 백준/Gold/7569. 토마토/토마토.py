import sys
from collections import deque


dx, dy, dz= [-1,0,1,0,0,0], [0,1,0,-1,0,0],[0,0,0,0,1,-1]


input=sys.stdin.readline

N,M,H=map(int,input().split())

graph=[[[] for _ in range(M)] for _ in range(H)]
start_point=[]

for k in range(H):
    floor=[]
    for i in range(M):
        row=list(map(int, input().split()))
        floor.append(row)

        for j, value in enumerate(row):
            if value == 1:
                start_point.append((i, j,k)) 
    graph[k]=floor

def bfs(graph, start_point):
    visited=[[[False]*N for _ in range(M)] for _ in range(H)]
    queue=deque()
    for points in start_point:
        queue.append(points)

    while queue:
        cx, cy, cz= queue.popleft()
        if visited[cz][cx][cy]==False:
            visited[cz][cx][cy]=True
        

        for i in range(6):
            nx,ny,nz=cx+dx[i], cy+dy[i], cz+dz[i]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H: 
                if visited[nz][nx][ny]==False and graph[nz][nx][ny]==0:
                    visited[nz][nx][ny]=True
                    graph[nz][nx][ny]=graph[cz][cx][cy]+1
                    queue.append((nx,ny,nz))
    return visited


bfs(graph, start_point)

max_val=0
for k in range(H):
    for i in range(M):
        for j in range(N):
            if graph[k][i][j]==0:
                print(-1)
                exit()

            max_val=max(max_val, graph[k][i][j])

print(max_val-1)