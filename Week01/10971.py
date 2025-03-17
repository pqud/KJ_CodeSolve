from itertools import permutations

N=int(input())

W=[[0]*N for _ in range(N)]

for i in range(N):
    W[i]=list(map(int, input().split()))

cities=[i for i in range(1,N)]
routes=list(permutations(cities))



min_cost=float('inf')
for route in routes:
    cost = 0
    valid = True
    
    # 시작 도시에서 첫 번째 도시로 이동
    if W[0][route[0]] != 0:
        cost += W[0][route[0]]
    else:
        continue  # 불가능한 경로는 스킵

    # 순열 내 도시 간 이동
    for i in range(len(route) - 1):
        if W[route[i]][route[i + 1]] != 0:
            cost += W[route[i]][route[i + 1]]
        else:
            valid = False
            break

    # 마지막 도시에서 시작 도시로 복귀
    if valid and W[route[-1]][0] != 0:
        cost += W[route[-1]][0]
    else:
        continue

    # 최소 비용 갱신
    if valid:
        min_cost = min(min_cost, cost)


print(min_cost)