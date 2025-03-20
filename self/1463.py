# 0.15초는 10^7 N은 10^6 시간복잡도 O(NlogN)까지


min_times=float('inf')

def make_1(n, count):
    global min_times


    if int(n) != n: 
        return
    
    if n==1:
        if min_times>count:
            min_times=count
        return count
    
    if count+1<=min_times:
        if n%3==0: 
            make_1(n/3,count+1)

        if n%2== 0:
            make_1(n/2, count+1)

        if n>1:
            make_1(n-1, count+1)



    
n = int(input())

make_1(n,0)
print(min_times)


