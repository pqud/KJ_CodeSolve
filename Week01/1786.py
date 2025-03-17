

#s가 아니라 p의 getpi를 합니다.
def getPi(p):
    m=len(p)
    j=0

    pi=[0 for _ in range(m) ]

    for i in range(1, m): #i는 1부터
        while j > 0 and p[i]!=p[j]:
            j=pi[j-1]
        if p[i]==p[j]: #prefix(p[i])와 surffix(p[j])가 동일하다면
            j+=1
            pi[i]=j 

    return pi

def kmp(s, p):
    ans=[]
    pi= getPi(p)

    n=len(s)
    m=len(p)
    j=0

    for i in range(n): #i는 s의 포인터. 0부터 
        while j>0 and s[i]!=p[j]:
            j=pi[j-1]
        if(s[i]==p[j]):
            if(j==m-1): #패턴을 찾았음
                ans.append(i-m+1)
                j=pi[j] 
            else:
                j+=1
    
    return ans


if __name__=='__main__':
    s=input()
    p=input()

    matched=kmp(s,p)
    print(len(matched))
    
    for item in matched:
        print(item+1)


