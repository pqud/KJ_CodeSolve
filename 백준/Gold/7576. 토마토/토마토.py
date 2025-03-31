import sys
from collections import deque


dx, dy= [-1,0,1,0], [0,1,0,-1]


input=sys.stdin.readline

N,M=map(int,input().split())

graph=[[] for _ in range(M)]
start_point=[]

for i in range(M):
    row=list(map(int, input().split()))
    graph[i]=row

    for j, value in enumerate(row):
        if value == 1:
            start_point.append((i, j)) 

def bfs(graph, start_point):
    visited=[[False]*N for _ in range(M)]

    queue=deque()
    for points in start_point:
        queue.append(points)

    while queue:
        cx, cy= queue.popleft()
        # print(cx,cy)
        # print(graph[cx][cy])
        if visited[cx][cy]==False:
            visited[cx][cy]=True
        
        for i in range(4):
            nx,ny=cx+dx[i], cy+dy[i]
            if 0<=nx<M and 0<=ny<N: 
                if visited[nx][ny]==False and graph[nx][ny]==0:
                    visited[nx][ny]=True
                    graph[nx][ny]=graph[cx][cy]+1
                    queue.append((nx,ny))

    return visited

bfs(graph, start_point)

# print(graph)

max_val=0
for i in range(M):
    for j in range(N):
        if graph[i][j]==0:
            print(-1)
            exit()

        max_val=max(max_val, graph[i][j])

print(max_val-1)