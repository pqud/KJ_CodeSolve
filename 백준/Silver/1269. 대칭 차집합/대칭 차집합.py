import sys

input=sys.stdin.readline

a,b=map(int, input().split())
temp=[]
for _ in range(2):
    temp.extend(map(int, input().split()))

m=set()

for num in temp:
    if num in m:
        m.remove(num)
    else:
        m.add(num)

print(len(m))