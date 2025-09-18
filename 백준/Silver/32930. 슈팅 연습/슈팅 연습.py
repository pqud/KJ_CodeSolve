import sys

input = sys.stdin.readline

N,M = map(int, input().split())
target = []
cur = [0,0]
answer=0

for _ in range(N):
    target.append(list(map(int, input().split())))

for i in range(M):
    max_dis = 0
    max_point = [0,0]

    for points in target:
        dis = (cur[0]-points[0])**2 +  (cur[1]-points[1])**2
        if max_dis < dis:
            max_dis = dis
            max_point = points
    
    answer+=max_dis
    cur=max_point
    target.remove(max_point)
    target.append(list(map(int, input().split())))

print(answer)