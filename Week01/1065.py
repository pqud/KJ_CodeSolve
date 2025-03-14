a= input()
n = int(a)


ans=0

if n <= 99:
    print(n)

else:
    for i in range (100, n+1):
        num=i
        num=str(num)

        if int(num[1])-int(num[0])==int(num[2])-int(num[1]):
            ans+=1
        

    

    print(ans+99)
    