from bisect import bisect_right

import sys

input= sys.stdin. readline

N,k = map(int, input().split())

coins=[]
for i in range(N):
    coins.append(int(input()))

idx=bisect_right(coins, k) #가장 큰 동전


answer=0
while k>0 :
    idx-=1
    cnt=k//coins[idx]
    k-=cnt*coins[idx]
    answer+=cnt
    

print(answer)