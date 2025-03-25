import sys

N=int(sys.stdin.readline())

stick=[]

for i in range(N):
    stick.append(int(sys.stdin.readline()))


ctn=1

H=stick.pop()

while stick:
    top=stick.pop()
    if top>H:
        H=top
        ctn+=1

print(ctn)

