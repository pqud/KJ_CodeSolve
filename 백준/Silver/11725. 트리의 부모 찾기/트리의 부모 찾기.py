import sys



def dfs(graph, start):
    n=len(graph)
    visited=[0]*(n+1)
    stack=[start]

    while stack:
        value=stack.pop()
        for i in graph[value]:
            if visited[i]==0: #방문안함함
                visited[i]=value
                stack.append(i)

    for i in range(2,len(visited)):
        print(visited[i])

if __name__ == "__main__":
    N=int(sys.stdin.readline())
    
    graph={}
    while True:
        try:
            line = sys.stdin.readline().strip()  
            # 입력이 비어 있거나, 두 개의 숫자가 아니면 중단
            if not line.strip() or len(line.split()) != 2:
                break

            a, b = map(int, line.split())
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)

        except ValueError:
            break

    dfs(graph,1)

   
    
    