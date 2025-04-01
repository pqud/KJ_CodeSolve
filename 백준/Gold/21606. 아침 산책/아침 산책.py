import sys

input=sys.stdin.readline

N=int(input())
 
inout=list(map(int, input().strip())) #1이면 실내 0이면 실외

start_point=[]

for i, val in enumerate(inout):
    if val==0: #실외면 스타트포인트에
        start_point.append(i+1)

outdoors=[]

graph=[[] for _ in range(N+1)]
route=0

for i in range(N-1):
    s, e= map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

    if inout[s-1]==1 and inout[e-1]==1:
        route+=2



visited=[False]*(N+1)

def dfs(graph, start):
    cnt = 0
    stack = [start]
    visited[start] = True  # 시작 노드 방문 체크

    while stack:
        node = stack.pop()

        for adj in graph[node]:
            if inout[adj - 1] == 0:  # 실외라면 계속 탐색
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)
            else:  # 실내라면 카운트 증가
                cnt += 1

    return cnt


result=0
#모든 스타트 지점(실외)에서 탐색을 해야함.
for start in start_point:
    if visited[start]==False:
        visited[start]=True
        result=dfs(graph, start)
        route+=result*(result-1)
print(route)