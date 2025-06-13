import sys

input=sys.stdin.readline

a,b=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
B_set=set(B)

A_minus_B=0
A_and_B=0

for i in A:
    if i not in B_set:
        A_minus_B+=1
    else:
        A_and_B+=1


print(A_minus_B+len(B)-A_and_B)