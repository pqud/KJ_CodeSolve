n=int(input())

k= n//5
result=n-5*k
# print(result)
while result<=n:
    if result%2==0:
        j=result//2
        print(k+j)
        exit()
    else:
        result+=5
        k-=1

print(-1)
