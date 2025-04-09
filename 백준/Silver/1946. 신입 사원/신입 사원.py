import sys

input=sys.stdin.readline

t=int(input())
for i in range(t):
    n=int(input())
    people=[]

    min_s=float('inf') #서류 점수수
    min_m=float('inf')#면접 점수
    cnt=0
    for i in range(n):
        s,m=map(int, input().split())
        people.append((s,m))
    
    people.sort(key=lambda x: (x[0]))
    # print(people)
    for peo in people:
        if peo[0]<min_s or peo[1]<min_m: #서류 점수나 면접 점수가 이전 최고 점수보다 크면 
            min_s=peo[0] 
            min_m=peo[1]
            cnt+=1
    print(cnt)

