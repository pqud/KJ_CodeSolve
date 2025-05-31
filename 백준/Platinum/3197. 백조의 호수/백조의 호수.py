import sys
from collections import deque

input=sys.stdin.readline
dx,dy=[-1,0,1,0],[0,1,0,-1]

R, C=map(int, input().split())

graph=[]
waters=[]

def solve():
    visited=[[False]*C for _ in range(R)]
    
    water_q=deque()
    n_water_q=deque()
    swan_q=deque()
    n_swan_q=deque()

    for i in range(R):
        for j in range(C):
            if graph[i][j] == '.' or graph[i][j] == 'L':
                water_q.append((i, j))
            if graph[i][j] == 'L':
                swan_start = (i, j)
    swan_q.append(swan_start)
    visited[swan_start[0]][swan_start[1]] = True

    days = 0
    while True:
        while swan_q:
            cy,cx=swan_q.popleft()
            for i in range(4):
                ny, nx=cy+dy[i], cx+dx[i]
                if 0<=ny<R and 0<=nx<C and not visited[ny][nx]:
                    if graph[ny][nx] == '.':
                        visited[ny][nx]=True
                        swan_q.append((ny,nx))
                    elif graph[ny][nx]=='L':
                        return days
                    elif graph[ny][nx]=='X':
                        visited[ny][nx]=True
                        n_swan_q.append((ny,nx))

        while water_q:
            cy, cx = water_q.popleft()
            for d in range(4):
                ny, nx=cy+dy[d], cx+dx[d]
                if 0<=ny<R and 0<=nx<C:
                    if graph[ny][nx]=='X':
                        graph[ny][nx]='.'
                        n_water_q.append((ny,nx))

        swan_q, n_swan_q = n_swan_q, deque()
        water_q, n_water_q = n_water_q, deque()
        days += 1

for i in range(R):
    row=list(input())
    graph.append(row[0:-1])

print(solve())