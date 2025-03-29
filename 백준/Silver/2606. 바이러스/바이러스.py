import sys

read=sys.stdin.readline


def dfs(graph, start):
    n=len(graph)
    visited=[False]*n
    stack=[start]

    while stack:
        value=stack.pop()
        if not visited[value]:
            visited[value]=True
            for i in range(n):
                if graph[value][i]==1 and not visited[i]:
                    stack.append(i)
        
    cnt=visited.count(True)

    return cnt-1




if __name__=="__main__":


    N= int(read())
    M= int(read())
    

    graph=[[0] * N for _ in range(N)]

    for i in range(M):
        u,v=map(int, read().split())
        u,v=u-1,v-1
        
        graph[u][v]=1
        graph[v][u]=1

    answer=0

    # print(graph)
    print(dfs(graph, 0))
    # print(answer)