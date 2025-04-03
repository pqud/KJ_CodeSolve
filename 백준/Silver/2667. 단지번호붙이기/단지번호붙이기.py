import sys
from collections import deque


#10분동안 열심히 풀었어요 

input=sys.stdin.readline
dx, dy=[-1,0,1,0], [0,1,0,-1]

N=int(input())

graph=[[] for _ in range(N)]

for i in range(N):
    row= list(input())
    graph[i]=row[0:-1]

# print(graph)


def bfs(start_x, start_y):
    queue=deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y]=True
    area=0

    while queue:
        cx, cy= queue.popleft()
        area+=1

        for i in range(4):
            nx, ny= cx+dx[i], cy+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if visited[nx][ny]==False and graph[nx][ny]=='1':
                    #범위 안에 있고 방문 안했고 값이 1이면 
                    visited[nx][ny]=True
                    queue.append((nx, ny))
    return area


visited=[[False]*N for _ in range(N)]
result=[]

for i in range(N):
    for j in range(N):
        if visited[i][j]==False and graph[i][j]=='1':
            result.append(bfs(i,j))


print(len(result))

result.sort()
for re in result:
    print(re)


    

