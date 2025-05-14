import sys
import heapq
input = sys.stdin.readline

N, C = map(int, input().split())


def find_Set(parent, node):
    if parent[node]!=node: #node의 부모가 node가 아니면(즉 node에게 부모가 있음)
        parent[node]=find_Set(parent, parent[node])
    return parent[node]


def union(parent, a, b):
    a=find_Set(parent, a)
    b=find_Set(parent, b)

    #부모가 더 큰 쪽을 새 부모 삼아서 합침
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


nodes=[]
for i in range(N):
    x, y= map(int, input().split())
    nodes.append([x,y])

parent=[_ for _ in range(N)]
edges=[]
total_cost=0
edge_num=0
pq=[]


for i in range(N):
    for j in range(i+1, N):
        ai, bi=nodes[i]
        aj, bj=nodes[j]
        cost=(ai-aj)**2 + (bi-bj)**2
        if cost>=C: heapq.heappush(pq, [cost, i, j])


while pq:
    cur_cost, node1, node2 = heapq.heappop(pq)
    
    if find_Set(parent,node1) != find_Set(parent,node2):
        total_cost+=cur_cost
        edge_num+=1
        union(parent, node1, node2)
        if edge_num==N-1 : break
if edge_num==N-1:print(total_cost)
else: print(-1)