import sys

N=int(sys.stdin.readline())
K= int(sys.stdin.readline())

apples=[]

for i in range(K):
    x,y=map(int, sys.stdin.readline().split())
    apples.append((x,y))

L=int(sys.stdin.readline())

di, dj=[-1,0,1,0], [0,1,0,-1] 
dt=[0]*10001

for i in range(L):
    x,c=sys.stdin.readline().split()
    x=int(x)
    dt[x]=c


dr=1
snake=[(1,1)]
answer=0

while True:
    answer+=1
    ci, cj=snake[0]
    ni, nj=ci+di[dr], cj+dj[dr]

    if 1<=ni<=N and 1<=nj<=N and (ni,nj) not in snake:
        snake.insert(0,(ni,nj)) #머리 위치(0)에 이동좌표 넣기 
        if (ni,nj) in apples:
            apples.remove((ni,nj))
        else:
            snake.remove((snake[-1]))
        
        if dt[answer]=="D": #우회전 명령
            dr=(dr+1)%4
        elif dt[answer]=='L': #좌회전 명령령
            dr=(dr+3)%4

    else:
        break

print(answer)