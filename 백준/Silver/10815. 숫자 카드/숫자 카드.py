import sys
from bisect import bisect_left

N=int(sys.stdin.readline())


cards=list(map(int,(sys.stdin.readline().split())))

cards.sort()

M=int(sys.stdin.readline())
targets=list(map(int,(sys.stdin.readline().split())))

answers=[]

for i in range(M):
    index=bisect_left(cards, targets[i])
    
    if index<len(cards) and targets[i]==cards[index]:
        answers.append("1")
    else:
        answers.append("0")

for answer in answers:
    print(answer, end=" ")
    