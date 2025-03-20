
answers=[]
answer=0

#북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

N= int(input())
A=[[0]*N for _ in range(N)]
graph=[[0]*N for _ in range(N)]

def dfs(x,y):
    global answer
    stack=[(x,y)]
    visited[x][y]=1

    while stack:
        cx, cy= stack.pop()
        visited[cx][cy]=1
        
        if 0<= cx< N and 0<= cy <N and graph[cx][cy]==0: 
            #현재 xy가 범위 내에 존재함함

            for i in range(4):
                #현재 xy의 상하좌우를 검색함함
                nx, ny = cx+dx[i], cy+dy[i] 
                if (0<= nx< N and 0<= ny <N and graph[nx][ny]==0 and visited[nx][ny]==0):
                    visited[nx][ny]=1
                    stack.append((nx,ny))
                    
    answer+=1
max_value=0

for i in range(N):
    # 한 줄에 공백으로 구분된 N개의 값을 정수형으로 변환
    row = list(map(int, input().split()))
    
    # 행렬에 저장
    A[i] = row
    
    # 행 내부의 각 원소에 대해 최대값 갱신
    for num in row:
        if num > max_value:
            max_value = num
        

for k in range(1, max_value+1):
    answer=0
    graph=[[0]*N for _ in range(N)]
    visited=[[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if A[i][j]<k:
                graph[i][j]=1 #k보다 작으면 물에 잠김김

    for i in range(N):
        for j in range(N):
            if graph[i][j]==0 and visited[i][j]==0: #물에 잠기지 않았고 방문하지 않았으면면
                dfs(i, j) 
    answers.append(answer)


    

print(max(answers))