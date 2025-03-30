import sys
from collections import deque

dx, dy=[-1,0,1,0], [0,1,0,-1]

def bfs(graph, start):
    n,m=len(graph), len(graph[0])
    queue=deque()
    queue.append((start))
    visited=[[False]*m for _ in range(n)]

    while queue:
        # print(queue)
        cx, cy,cnt= queue.popleft()
        if visited[cx][cy]==False:
            visited[cx][cy]=True
            #value 노드의 상,하,좌,우를 살펴야함!
        if cx==n-1 and cy==m-1:
            return cnt
        for i in range(4):
            nx, ny= cx+dx[i], cy+dy[i]
            if 0 <= nx < n and 0 <= ny < m:  # 그래프 범위 체크
                if graph[nx][ny]=='1' and visited[nx][ny]==False :
                    visited[nx][ny]=True
                    queue.append((nx,ny,cnt+1)) 

        


input=sys.stdin.readline

N,M=map(int, input().split())

graph=[[0]for _ in range(N)]


for i in range(N):
    row=list(input())
    row=row[0:-1]

    graph[i]=row

print(bfs(graph, (0,0,1)))




