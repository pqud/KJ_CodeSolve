import sys



input_string=sys.stdin.readline()
values = list(input_string)

values.pop() # 개행문자 빼야함함

bracket=[]
tmp=1
answer=0


for i in range(len(values)):
    if values[i]=="(":
        bracket.append(values[i])
        tmp*=2

    elif values[i]=="[":
        bracket.append(values[i])
        tmp*=3

    elif values[i]==")":
        if not bracket or bracket[-1]=="[": 
            #value의 마지막 값이 [면 PS가 아님
            answer=0
            break 
        if values[i-1]=="(": #한 쌍이 되면 
            answer+= tmp
        bracket.pop()
        tmp//=2

    else: #values[i]=="]":
        if not bracket or bracket[-1]=="(":
            answer=0
            break
        if values[i-1]=="[": # 한 쌍이 되면 
            answer+=tmp

        bracket.pop()
        tmp//=3

if bracket:
    print(0)
else:
    print(answer)