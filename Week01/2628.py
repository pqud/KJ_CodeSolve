w, h = map(int, input().split())
number=int(input()) #잘라야 하는 횟수


vertical=[0]
horizontal=[0]
width_list=[]

for _ in range(0, number):
    #axis 0은 가로 1은 세로로
    axis, line_number = map(int, input().split())
    if axis==0:
        horizontal.append(line_number)
    else:
        vertical.append(line_number)

vertical.append(w)
horizontal.append(h)

vertical.sort()
horizontal.sort()


for i in range(0, len(vertical)-1):
    for j in range(0,len(horizontal)-1):
        width=abs((vertical[i+1]-vertical[i])*(horizontal[j+1]-horizontal[j]))
        width_list.append(width)
        

print(max(width_list))