N=int(input())

a=[]

for i in range(N):
    a.append(int(input()))


a.sort()

for item in a:
    print(item)