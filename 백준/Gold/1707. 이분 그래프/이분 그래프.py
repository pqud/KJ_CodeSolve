
import sys
sys.setrecursionlimit(10 **5 )


T=int(sys.stdin.readline())

def dfs(graph, start, visited):
    stack = [start]
    visited[start] = 'R'  # 첫 번째 노드를 R로 칠함

    while stack:
        value = stack.pop()

        for i in graph[value]:
            if not visited[i]:  # 방문하지 않았다면 부모와 반대 색으로 칠함
                visited[i] = 'B' if visited[value] == 'R' else 'R'
                stack.append(i)
            elif visited[value] == visited[i]:  # 같은 색이면 이분 그래프 아님
                print("NO")
                return False

    for i in range(1, V+1):
        if visited[i]==False:
            return dfs(graph,i,visited)
    return True

for i in range(T):
    V,E= map(int, sys.stdin.readline().split())

    graph={}

    for j in range(V+1):
        graph[j]=[]

    for j in range(E):
        #지금 입력 들어오는게 V가 5면 노드가 1부터 5까지 있긴 한데 아예 다른거랑 연결 안 된 노드가 존재함...
        u, v = map(int,sys.stdin.readline().split())
        graph[v].append(u)
        graph[u].append(v)
    
    visited=[False]*(V+1)

    flag=dfs(graph, u, visited)


    if flag==True and False not in visited[1:]:
        print("YES")
