A, B, C= int(input()) , int(input()), int(input())

result= str(A*B*C)

for i in range(10):
    print(result.count(str(i)))
