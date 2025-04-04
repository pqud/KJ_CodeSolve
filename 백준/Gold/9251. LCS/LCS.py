s1=list(input())
s2=list(input())

s1.insert(0, 0)
s2.insert(0, 0)


dp=[[0]*len(s2) for _ in range(len(s1))]


for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0 or j == 0: # 둘 중 한 문자열의 길이가 0이라면 
            dp[i][j]=0

        elif s1[i]==s2[j]: #s2와 s1 중 겹치는게 있다면 
            dp[i][j] = dp[i-1][j-1]+1 
        
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

# print(dp)

print(dp[len(s1)-1][len(s2)-1])