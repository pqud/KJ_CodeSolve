import sys

input=sys.stdin.readline

fac_num=int(input())
factory=list(map(int, input().split()))+[0,0]
total=0


def buy1(n): # 1개 살 경우
    global total
    total += 3 * factory[n]

def buy2(n): # 2개 살 경우
    global total
    m = min(factory[n:n+2])
    factory[n] -= m
    factory[n+1] -= m
    total += 5* m    

def buy3(n): # 3개 살 경우
    global total
    m = min(factory[n:n+3])
    factory[n] -= m
    factory[n+1] -= m
    factory[n+2] -= m
    total += 7* m


for i in range(len(factory)-2):
    if factory[i+1] > factory[i+2]: 
        m = min(factory[i], factory[i+1] - factory[i+2]) 
        factory[i] -= m
        factory[i+1] -= m
        total += 5*m
        buy3(i)
        buy1(i) 
    else :
        buy3(i)
        buy2(i)
        buy1(i)

print(total)

