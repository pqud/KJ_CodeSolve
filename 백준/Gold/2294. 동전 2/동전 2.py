import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int, input().split())
coins=[]


for _ in range(n):
    coins.append(int(input()))

dp=[float('inf')] * (m+1)
dp[0]=0

for coin in coins:
    for i in range(coin, m+1) :
        dp[i]=min(dp[i], dp[i-coin]+1)

if dp[m]==float('inf'):
    print(-1)
else:
    print(dp[m])