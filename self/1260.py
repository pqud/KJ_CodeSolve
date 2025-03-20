import copy
from collections import deque

N, M, V= map(int, input().split())
dfs_graph=[[] for _ in range(N+1)]

dfs_order=[]
bfs_order=[]


for i in range(M):
    start, end = map(int, input().split())
    dfs_graph[start].append(end)
    dfs_graph[end].append(start)



bfs_graph=copy.deepcopy(dfs_graph)

for i in range(N+1):
    # print(dfs_graph[i])
    dfs_graph[i].sort(reverse=True)
    # print(dfs_graph[i])
    bfs_graph[i].sort()

# print(dfs_graph)


def dfs(n, graph, start):
    #스택을 씀
    visited=[False]*(n+1)

    stack=[start]

    while stack:
        # print(stack)
        value=stack.pop()
        if not visited[value]:
            dfs_order.append(value)
            visited[value]=True
            for j in graph[value]:
                if not visited[j]:
                    stack.append(j)


def bfs(n, graph, start):
    #큐를 씀
    
    visited=[False]*(n+1)

    queue=deque()
    queue.appendleft(start)

    while queue:
        # print(queue)
        value=queue.popleft()
        if not visited[value]:
            bfs_order.append(value)
            visited[value]=True
            for j in graph[value]:
                if not visited[j] :
                    queue.append(j)
            


dfs(N, dfs_graph, V)
bfs(N, bfs_graph, V)

for i in dfs_order:
    print(i, end=" ")
print()
for j in bfs_order:
    print(j,end=" ")
