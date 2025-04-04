n=int(input())

fibo_result=[0]*91
fibo_result[1]=1

for i in range(2, n+1):
    fibo_result[i]=fibo_result[i-1]+fibo_result[i-2]

print(fibo_result[n])
