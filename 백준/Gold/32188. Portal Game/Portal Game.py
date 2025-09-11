import sys
from collections import deque


input = sys.stdin.readline
n, c = map(int, input().split())



portals = [[] for _ in range(n)]
queue=deque()
INF=1e9
visited=[INF] * n
answer=INF

queue.append((0,0))

for _ in range(c):
    type, start, end = map(int, input().split())
    portals[start].append((end, type)) 

while(queue):
    flag=False
    cur, curtime = queue.popleft()

    if visited[cur]>curtime:
        visited[cur]=curtime
    else:
        continue

    if cur == n-1:
        answer=min(answer, curtime)
        break

    for e,t in portals[cur]:
        if t== 1: #블루 포탈
            queue.appendleft((e, curtime))
            queue.append((cur+1, curtime+1))
            flag=True

        elif t==0:
            queue.appendleft((e, curtime))
            flag=True

    if(flag is False):
        queue.append((cur+1, curtime+1))


print(answer if answer != INF else -1)
