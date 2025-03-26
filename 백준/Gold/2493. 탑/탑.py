import sys

N=int(sys.stdin.readline())

temp=[]
inputs=[]

inputs=list(map(int,sys.stdin.readline().split()))
heights = [[index, value] for index, value in enumerate(inputs)]



answers=[0]*N


for i in range(N): #가장 오른쪽에 있는 탑이 가장 크다면 0이어야 함! 그 경우를 처리 못하는 중

    h_top=heights.pop()

    if temp:
        t_top= temp[-1]
    else:
        temp.append(h_top)
        continue

    if h_top[1]<t_top[1]:
        temp.append(h_top)

    else:
        while temp and h_top[1] > temp[-1][1]:  # 조건을 while문 자체에 포함
            answers[temp[-1][0]]=h_top[0]+1
            temp.pop()
        temp.append(h_top)  # while문 종료 후 append

# while temp: #heights에서 다 꺼냈는데 temp에 남아있다면
#     answers[temp[-1][0]]=0
#     temp.pop()
        

for answer in answers:
    sys.stdout.write(str(answer) + " ")