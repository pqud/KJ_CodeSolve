import sys
from collections import deque

input=sys.stdin.readline

n=int(input())
m=int(input())

indegree=[0]*(n+1)
needs=[[0]*(n+1) for _ in range(n+1)]
nodes={}
base=[] #기본 노드. 예시에서 [1,2,3,4].


for _ in range(m):
    a,b,w=map(int, input().split())
    if a not in nodes:
        nodes[a]=[]
    if b not in nodes:
        nodes[b]=[]

    nodes[b].append((a,w))
    indegree[a]+=1

for i in range(1, n+1):
    if(indegree[i]==0):
        base.append(i)

base_len=len(base)
# print(base)
# print(nodes)
# print(indegree)


queue=deque()
for i in base:
    queue.append(i)

while queue:
    cur_node=queue.popleft()

    for next_node, weight in nodes[cur_node]:
        if cur_node in base: #기본 부품으로만 만들 수 있는 장난감이면
            needs[next_node][cur_node]+=weight #해당 장난감 추가.

        for i in range(1,n+1):
            #다음 노드는 (현재 노드가 필요했던 양)*(자기 분 weight)만큼 필요로 함. 
            needs[next_node][i]+=needs[cur_node][i]*weight 
        
        indegree[next_node]-=1 #진입차수 감소
        if indegree[next_node]==0: #진입차수 0 되면 큐에 추가
            queue.append(next_node)

# print(needs)

for i in base:
    print(i, needs[n][i])