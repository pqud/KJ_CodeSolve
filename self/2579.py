N=int(input())

Stairs=[]
for i in range(N):
    Stairs.append(int(input()))

Stairs.reverse() #역순으로 계산
dp=[[0,0] for _ in range(N)]

dp[0][0]=Stairs[0] #첫번째 계단(실제론 마지막 계단)은 무조건 밟아야 함

if N>1:
    dp[1][0]=Stairs[1]+Stairs[0]
    dp[1][1]=-1



for i in range(2, N):
    dp[i][0]=dp[i-1][1]+Stairs[i]
    dp[i][1]=max(dp[i-2])+Stairs[i] if dp[i-1] !=-1 else -1

print(max(dp[N-1][0],dp[N-1][1], dp[N-2][0],dp[N-2][1]))