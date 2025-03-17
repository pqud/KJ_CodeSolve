
counter=[[] for i in range(50)]

if __name__=='__main__':
    N=int(input())


    for i in range(N):
        a = input()
        k= len(a)
        counter[k-1].append(a)
        
    for i in range(50):
        counter[i] = sorted(set(counter[i])) 



    for i in range(50):
        k= len(counter[i])
        if k!=0:
            for j in range(k):
                print(counter[i].pop(0))

