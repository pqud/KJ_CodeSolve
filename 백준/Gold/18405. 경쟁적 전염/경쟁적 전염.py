import sys
import heapq
import copy

input=sys.stdin.readline
dx, dy=[-1,0,1,0], [0,1,0,-1]

N,K=map(int, input().split()) #K는 바이러스의 최대 숫자. 1~K까지의 바이러스가 있음.

graph=[[] for _ in range(N)]
virus_list=[]

for i in range(N):
    row = list(map(int, input().split()))
    graph[i]=row

    for j in range(N):
        if row[j] != 0:  # 바이러스가 있는 위치 저장
            heapq.heappush(virus_list, (row[j], i, j))  # (바이러스 번호, x, y)     


S, X, Y= map(int, input().split())
# S초 뒤에 (X,Y)에 존재하는 바이러스의 종류를 구하시오.

for _ in range(S):

    next_virus=[]
    while virus_list:
        type, cx, cy = heapq.heappop(virus_list)

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = type
                next_virus.append((type, nx, ny))

    for vir in next_virus: 
        heapq.heappush(virus_list, vir)
    
    # print(virus_list)
    # print(graph)

print(graph[X-1][Y-1])



