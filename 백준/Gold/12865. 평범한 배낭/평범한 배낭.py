N, K= map(int,input().split()) #N은 물건의 수, K는 버틸 수 있는 무게 

obj = [0]*(N+1)

for i in range(1, N+1):
    w, b= map(int, input().split()) #무게, 가치 한 쌍쌍 
    obj[i]=(w, b)

# print(obj)

dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for w in range(1, K+1):
        wi=obj[i][0]
        vi=obj[i][1]
        if wi>w:
            dp[i][w]=dp[i-1][w] # 그 전걸(테이블 상 윗 쪽 값) 그대로 이어감.
        else: 
            dp[i][w]=max(dp[i-1][w], dp[i-1][w-wi]+vi)

print(dp[N][K])