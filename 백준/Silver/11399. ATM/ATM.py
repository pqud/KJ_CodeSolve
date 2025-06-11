N= int(input())

P=list(map(int, input().split()))
times=[]

P.sort()
times.append(P[0])

for i in range(1, N):
    times.append(P[i]+times[i-1])

print(sum(times))