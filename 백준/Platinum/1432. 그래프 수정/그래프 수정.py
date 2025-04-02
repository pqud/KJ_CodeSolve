import sys
import heapq

#무방향 그래프

input=sys.stdin.readline

N=int(input())

graph=[[] for _ in range(N+1)]
result=[0]*(N+1)
outdegree=[0]*(N+1)

for i in range(1,N+1):
    row=list(input())
    for j, val in enumerate(row, start=1):
        if val=='1': #1이면 연결된거임 
            outdegree[i]+=1
            graph[j].append(i)  


max_heap=[]
for i in range(1, N+1):
    if outdegree[i]==0: #outdegree 차수 0인 노드 큐에 추가함
        heapq.heappush(max_heap, -i)


Num=N #N부터 1까지 숫자를 부여할 예정임
while max_heap:
    cur_node=-heapq.heappop(max_heap)
    result[cur_node]=Num
    Num-=1

    for adj in graph[cur_node]:
        outdegree[adj]-=1
        if outdegree[adj]==0:
            heapq.heappush(max_heap, -adj)




if result[1:].count(0)>0: #0이 한개라도 있으면 위상정렬 못한거 == 사이클 존재 == -1 찍기 
    print(-1)
else:
    for re in result[1:]:
        print(re, end=" ")
