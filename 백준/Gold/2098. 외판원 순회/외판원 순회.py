from itertools import combinations

N = int(input())
W = [[0] * (N + 1)]
for _ in range(N):
    W.append([0] + list(map(int, input().split())))

cities = [i for i in range(2, N + 1)]
dp = {}

# 기저 조건: i에서 1로 바로 가는 경로
for city in cities:
    dp[(city, ())] = W[city][1] if W[city][1] else float('inf')

# 모든 부분 집합에 대해 dp 계산
for r in range(1, len(cities) + 1):
    for A in combinations(cities, r):
        A = tuple(sorted(A))  # 정렬 보장
        for i in range(2, N + 1):
            if i in A:
                continue
            min_cost = float('inf')
            for j in A:
                if W[i][j] == 0:
                    continue
                A_minus_j = tuple(k for k in A if k != j)
                prev = dp.get((j, A_minus_j), float('inf'))
                cost = W[i][j] + prev
                min_cost = min(min_cost, cost)
            dp[(i, A)] = min_cost

# 최종 결과 계산: 1 → A → 1
A_all = tuple(sorted(cities))
min_total_cost = float('inf')
for j in A_all:
    if W[1][j] == 0:
        continue
    A_minus_j = tuple(k for k in A_all if k != j)
    prev = dp.get((j, A_minus_j), float('inf'))
    cost = W[1][j] + prev
    min_total_cost = min(min_total_cost, cost)

print(min_total_cost)
