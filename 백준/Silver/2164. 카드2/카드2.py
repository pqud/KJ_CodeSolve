import sys
from collections import deque

N=int(sys.stdin.readline())

Q= deque([x for x in range(N,0,-1)])


for i in range(N-1):    
    Q.pop()
    a=Q.pop()
    Q.appendleft(a)

print(Q.popleft())
    


