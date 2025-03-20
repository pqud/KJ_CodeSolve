N=input()
count=0

if len(N)==1:
    N="0"+N

target=N

while True:
    front=N[0]
    back=N[1]

    result=int(front)+int(back)

    if result<10:
        N=back+str(result)
    else:
        N=back+str(result)[1]

    count+=1
    if N==target:
        break

print(count)