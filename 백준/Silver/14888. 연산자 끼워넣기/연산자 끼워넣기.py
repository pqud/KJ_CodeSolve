import sys
import copy
from itertools import permutations

input=sys.stdin.readline

N=int(input())
nums=list(map(int, input().split()))
oper=list(map(int, input().split()))



min_ans=float('inf')
max_ans=float('-inf')

def dfs(plus, minus, mul, div, x, sum):
    global min_ans
    global max_ans

    if x== N-1:
        if sum<min_ans:
            min_ans=sum
        if sum>max_ans:
            max_ans=sum
        
    if plus>0:
        dfs(plus-1, minus, mul,div,x+1, sum+nums[x+1])
    if minus>0:
        dfs(plus, minus-1, mul,div,x+1, sum-nums[x+1])
    if mul>0:
        dfs(plus, minus, mul-1,div,x+1, sum*nums[x+1])
    if div>0:
        if sum<0:
            dfs(plus, minus, mul,div-1,x+1, -((-sum)//nums[x+1]))
        else:
            dfs(plus, minus, mul,div-1,x+1, sum//nums[x+1])
    
dfs(oper[0],oper[1],oper[2],oper[3],0,nums[0])

print(max_ans)
print(min_ans)