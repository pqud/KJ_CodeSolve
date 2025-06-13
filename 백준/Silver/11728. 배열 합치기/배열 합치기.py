import sys

input=sys.stdin.readline

n, m = map(int, input().split())

A=list(map(int, input().split()))
B=list(map(int, input().split()))
C=[]
last_idx=0

for i in range(n):
    for j in range(last_idx, m):
        if A[i]>B[j]:
            C.append(B[j])
            last_idx=j+1
        else:
            break
    C.append(A[i])

for i in range(last_idx, m):
    C.append(B[i])

for i in C:
    print(i, end=" ")