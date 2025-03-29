import sys

input=sys.stdin.readline

n=int(input()) #노드수
m=int(input()) #간선수수

graph=[[float('inf')] * (n+1) for _ in range(n+1)]

#자기 자신으로 돌아오는 비용은 0으로 초기화
for i in range(1, n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

#각 간선에 대한 정보를 입력받고 초기화
for _ in range(m):
    i, j, cost=map(int, input().split())
    graph[i][j]=min(cost, graph[i][j]) #동일한 간선이 여러개 있을 수 있음. 

#이하 워샬 알고리즘
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j]=min(graph[i][j], graph[i][k]+ graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==float('inf'):
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

