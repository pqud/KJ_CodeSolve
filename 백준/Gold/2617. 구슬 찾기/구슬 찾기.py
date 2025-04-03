import sys

input= sys.stdin.readline

N,M=map(int, input().split())

nodes_origin={}
nodes_reverse={}

result=[0]*(N+1)

for i in range(1, N+1):
    nodes_origin[i]=[]
    nodes_reverse[i]=[]

for i in range(M):
    a, b= map(int, input().split()) 
    
    nodes_origin[b].append(a) #b와 연결된 노드들 (정방향)
    nodes_reverse[a].append(b) #a와 연결된 노드들 (역방향)

def dfs(list, start):
    visited = set()
    stack = [(start)]
    depth = 0  # 최대 깊이 저장

    while stack:
        cur_node = stack.pop()
        if cur_node not in visited:
            visited.add(cur_node)
            depth +=1
            for adj in list[cur_node]:
                if adj not in visited:
                    stack.append((adj))
        

    return depth-1
     
mid=(N+1)//2
cnt=0


for i in range(1, N+1):
    if dfs(nodes_origin, i) >= mid:
        cnt+=1
    if dfs(nodes_reverse,i) >=mid:
        cnt+=1

print(cnt)
