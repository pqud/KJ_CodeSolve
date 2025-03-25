import sys

N=int(sys.stdin.readline().strip())

for i in range(N):

    input_string=sys.stdin.readline()
    values = list(input_string)

    values.pop() # 개행문자 빼야함함

    temp=[]

    while values:
        #temp가 비었을 때 top가 "(면 no임"
        if temp:
            top=values.pop()
            pair=temp[-1]

            if top=="(" and pair==")":
                temp.pop()
                continue
            else:
                temp.append(top)  
        else:
            top=values.pop()
            if top=="(":
                temp.append("")
                break
            else:
                temp.append(top)  

    if temp:
        print("NO")
    else:
        print("YES")