c= int(input())

for i in range(c):
    count=0
    score=list(map(int, input().split()))

    N=score[0]

    avg=sum(score[1:])/N
    for a in score[1:]:
        if a>avg:
            count+=1
    
    print("{:.3f}%".format(count/N*100))