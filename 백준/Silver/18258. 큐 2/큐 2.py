import sys

N=int(sys.stdin.readline())

commands=[]
for i in range(N):
    commands.append(sys.stdin.readline().split())

queue=[]
pointer=0
size=0

for command in commands:
    if command[0]=='pop':
        if size>0:
            print(queue[pointer])
            size-=1
            pointer+=1
        else:
            print("-1")

    elif command[0]=='size':
        print(size)

    elif command[0]=='empty':
        if size==0:
            print('1')
        else:
            print('0')

    elif command[0]=='front':
        if size>0:
            print(queue[pointer])
        else:
            print('-1')

    elif command[0]=="back":
        if size>0:
            print(queue[-1])
        else:
            print('-1')

    else: #push
        queue.append(command[1])
        size+=1
        
