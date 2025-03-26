import sys
import bisect

N=int(sys.stdin.readline())

circles=[]



for i in range(N):
    x,r=map(int,sys.stdin.readline().split())
    circles.append([x-r,'('])
    circles.append([x+r,')'])

circles.sort(key=lambda x: (x[0], x[1] == '('))

temp=[]
area=1

for i in range(N*2):
    position, bracket= circles[i]
    if len(temp)==0:
        temp.append({'pos':position, 'bracket':bracket, 'status':0})
        continue

    
    if bracket == "(":
        if temp and temp[-1]['pos']==position:
            temp[-1]['status']=1
        temp.append({'pos':position, 'bracket':bracket, 'status':0})

        #status 0:기본값
        # status 1: 원 안의 원이 연결되어 있다
        # 괄호가 닫혔을 때 status가 0이면 +1 1이면 +2

    elif bracket==")":
        if temp[-1]['status']==0:
            area+=1
        else:
            area+=2

        temp.pop()

        if i+1<len(circles):
            next=circles[i+1]
            if temp and next[0]!=position:
                temp[-1]['status']=0


print(area)