import sys
from collections import deque

input=sys.stdin.readline

n,m=map(int, input().split())
coins=[]


for _ in range(n):
    coins.append(int(input()))

def mincoin_dfs(target):
    queue=deque()
    queue.append((0,0)) #(총합, 현재 코인 개수) 가 쌍으로 들어감

    visited=set()
    visited.add((0,0))

    while queue:
        cur_hap, coin_count = queue.popleft()

        if cur_hap==target:
            return coin_count
        
        for coin in coins:
            next_hap = cur_hap+coin
            if next_hap <=target and next_hap not in visited:
                visited.add(next_hap)
                queue.append((next_hap, coin_count+1))

    return -1

print(mincoin_dfs(m))

