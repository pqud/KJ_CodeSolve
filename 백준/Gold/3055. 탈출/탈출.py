import sys
from collections import deque

input=sys.stdin.readline

dx,dy=[-1,0,1,0], [0,1,0,-1]

R, C =map(int,input().split())

graph=[]
waters=[]
start=0
end=0

for i in range(R):
    row= list(input())
    graph.append(row[0:-1])

    for j, value in enumerate(row):
        if value=='D':
            end=(i,j)
        if value=='S':
            start=(i,j)
            graph[i][j]=0
        if value=='*':
            waters.append((i,j))
# print(graph)

def dfs(graph, start, waters):
    visited=[[False]*C for _ in range(R)]

    queue=deque()
    for i in waters:
        queue.append(i)
    queue.append(start)
    

    while queue:
        cx, cy = queue.popleft()
        if not visited[cx][cy]:
            visited[cx][cy]=True
        
        for i in range(4):
            nx, ny=cx+dx[i], cy+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if graph[cx][cy]=='*': #물은 번지고고
                    # print(nx,ny)
                    # print(graph)
                    if graph[nx][ny]=='.':
                        graph[nx][ny]='*'
                        queue.append((nx,ny))
                        visited[nx][ny]=True
                else: #비버는 이동하고 
                    # print(f"when cx/cy: {graph[cx][cy]} nx/ny: {graph[nx][ny]}")
                    if graph[nx][ny]=='.':
                        graph[nx][ny]=graph[cx][cy]+1
                        queue.append((nx,ny))
                        visited[nx][ny]=True
                    elif graph[nx][ny]=='D':
                        return graph[cx][cy]+1
    return "KAKTUS"
                    

print(dfs(graph, start, waters))