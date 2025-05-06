import sys
input=sys.stdin.readline

n=int(input())
A,B= map(int,input().split())
m=int(input())
graph=[[] for _ in range(n+1)]
is_leaf=[True] * (n+1)


def dfs(start, target):
    stack=[(start,0)]
    visited=[False]*(n+1)

    while(stack):
        cur, depth=stack.pop()
        if cur==target:
            return depth
        
        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] =True
                stack.append((adj, depth+1))

    return -1

for _ in range(m):
    pa,child=map(int,input().split())
    graph[pa].append(child)
    graph[child].append(pa)
    is_leaf[pa]=False

# print(graph)
answer1=dfs(A,B)
answer2=dfs(B,A)

if answer1 == -1 or answer2 == -1:
    print(-1)
else:
    answer=min(answer1, answer2)
    print(answer)

