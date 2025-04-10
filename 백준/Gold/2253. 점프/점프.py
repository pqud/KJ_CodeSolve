import sys

input=sys.stdin.readline

n, m= map(int, input().split())
cant=list(int(input()) for _ in range(m))

#dp[i][j]는 속도 i로 돌 j로 도착하는 최소 점프 횟수.
dp=[[float('inf')]*(n+1) for _ in range(150)] 

if 2 not in cant:
    dp[1][2]=1

for x in range(1,n+1): #돌 좌표 x
    for s in range(1, 150): #속도 
        if dp[s][x]!=float('inf'):
            for ns in (s-1, s, s+1): #새로운 속도
                if ns<1:
                    continue
                nx= x+ ns
                if nx <=n and nx not in cant:
                    dp[ns][nx]=min(dp[ns][nx], dp[s][x]+1)

answer=min(dp[i][-1] for i in range(150))
print(answer if answer!=float('inf') else -1)