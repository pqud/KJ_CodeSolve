import sys
from collections import deque

# 1. 각 타일의 모양을 파악한다.
# 2. 타일의 모양에 따라서, 이동할 수 있는 방향을 정한다.
#   - 모양의 타일이면 양옆으로 검사한다.
#   | 모양 타일이면 위아래로 검사한다.
# 3. 이동할 수 있는 방향에 따라서, 타일의 모양을 비교한다.
# 4. 타일의 모양이 같으면, 값을 유지한다.
# 5. 타일의 모양이 다르면, 값을 증가시킨다.

input=sys.stdin.readline

# 그래프에서 값을 하나씩 검사.
# 값이 -면 오른쪽으로 검사하고 |면 아래로 검사해서 같으면 answer=answer, 다르면 answer+1

N, M = map(int, input().split())
graph=[[] for _ in range(N)]

for i in range(N):
    row=list(input())
    graph[i]=row[0:-1]

answer=0

visited=[[False]*M for _ in range(N)]

for i in range(N):

    for j in range(M):

        # print(f"i: {i}, j: {j} | {visited[i][j]}")
        if visited[i][j]==False: 
            answer+=1
            visited[i][j]=True

        if graph[i][j]=='-': #- 면 오른쪽으로만 검사해도 됨.     
            if j+1<M and visited[i][j+1]==False:
                if graph[i][j+1]=='-':
                    visited[i][j+1]=True #방문처리
               

        elif graph[i][j]=='|': #| 면 아래쪽으로만 검사해도 됨.     
            if i+1<N and visited[i+1][j]==False:
                if graph[i+1][j]=='|':
                    visited[i+1][j]=True #방문처리
               


print(answer)

