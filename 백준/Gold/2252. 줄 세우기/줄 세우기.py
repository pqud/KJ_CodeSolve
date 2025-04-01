import sys
from collections import deque

#무방향 그래프

input=sys.stdin.readline

N,M=map(int,input().split())

nodes={}
indegree=[0]*(N+1)

for i in range(M):
    a,b=map(int, input().split())
    if a not in nodes:
        nodes[a]=[]
    if b not in nodes:
        nodes[b]=[]

    nodes[a].append(b)
    indegree[b]+=1



queue=deque()
answers=[]

for i, val in enumerate(indegree[1:], start=1):
    if val == 0:
        queue.append(i)

while queue:
    val=queue.popleft()
    answers.append(val)
    # print(indegree)

    if val in nodes:
        for i in nodes[val]:
            indegree[int(i)]-=1
            
            if indegree[int(i)]==0:
                queue.append(i)

    # print(indegree)

for ans in answers:
    print(ans, end=" ")