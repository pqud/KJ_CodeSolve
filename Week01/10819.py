
def permutations(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in permutations(array[:i]+array[i+1:], r-1):
                yield [array[i]] + next




if __name__=="__main__":
    N=int(input())
    temp=[]

    
    A=list(map(int, input().split()))

    for perm in permutations(A,N):
        result=0
        for i in range(N-1):
            result+=abs(perm[i]-perm[i+1])
        temp.append(result)

    print(max(temp))