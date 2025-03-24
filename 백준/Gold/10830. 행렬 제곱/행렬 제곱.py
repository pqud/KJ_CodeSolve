import sys

N, B = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 행렬 곱셈 함수 (나머지 연산 적용)
def dot(X, Y):
    Z = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                Z[i][j] += X[i][k] * Y[k][j]
            Z[i][j] %= 1000  # 나머지 연산 적용해서 큰 수 방지
                
    return Z

# 메모이제이션을 위한 딕셔너리
Cal_Save = {}

# 분할 정복 방식으로 행렬의 거듭제곱을 구하는 함수
def divcon(A, B):
    if B in Cal_Save:
        return Cal_Save[B]

    # 기저 사례: B == 1이면 A 반환
    if B == 1:
        return [[A[i][j] % 1000 for j in range(N)] for i in range(N)]
    
    # B가 짝수일 때
    if B % 2 == 0:
        half = divcon(A, B // 2)
        Cal_Save[B] = dot(half, half)
    
    # B가 홀수일 때
    else:
        half_l = divcon(A, (B // 2)+1 )
        half_r = divcon(A, B // 2 )
        Cal_Save[B] = dot(half_l, half_r)
    
    return Cal_Save[B]

# 결과 행렬 계산
result = divcon(A, B)

# 결과 출력
for row in result:
    print(" ".join(map(str, row)))
