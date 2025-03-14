import math


# 달팽이는 n일 동안 A 미터 올라고 B 미터 미끄러집니다.
# 그러니까 V<=(A-B)*n이 되는 n 값을 구해야합니다.
# 이때 달팽이가 막대를 모두 올라가면 미끄러지지 않으므로
# V<=A*n-B(n-1)이 됩니다. 
# 그냥 풀면 시간초과남


A, B, V = map(int, input().split())

n= math.ceil((V-B)/(A-B))

print(int(n))