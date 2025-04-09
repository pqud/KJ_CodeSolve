import sys

input=sys.stdin.readline

n=int(input())

values=[]
for i in range(n):
    s,e=map(int, input().split())
    values.append((s,e))

values.sort(key=lambda x: (x[1], x[0]))


cnt=0
cur_time=0
for i in range(n):
    if values[i][0]>=cur_time:
        cur_time=values[i][1]
        cnt+=1

print(cnt)
