def makeNum(targetNum, temp):
    if sum(temp) == targetNum:
        yield temp
        return

        
    if sum(temp)> targetNum:
        return 

    for num in [1,2,3]:        
        yield from makeNum(targetNum, temp+[num])
   


T=int(input())
for i in range(T):
    N=int(input())
    answer=0
    temp=[]
    for i in makeNum(N, temp) :
        answer+=1

    print(answer)