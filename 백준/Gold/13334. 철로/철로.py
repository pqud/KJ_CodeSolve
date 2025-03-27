import sys
from bisect import bisect_left
import heapq

N=int(sys.stdin.readline())


positions=[]
for i in range(N):
    x1,x2=map(int, sys.stdin.readline().split())

    if x1>x2:
        x1,x2=x2,x1

    positions.append([x1,x2])

L=int(sys.stdin.readline())
# 끝점을 기준으로 정렬 (x2 기준 오름차순)
positions.sort(key=lambda x: x[1])

heap = []  # 최소 힙 (시작점 저장)
answer = 0

for x1, x2 in positions:
    # x2 - L 미만의 값은 제거 (범위를 벗어난 선분들)
    while heap and heap[0] < x2 - L:
        heapq.heappop(heap)

    # 현재 선분의 시작점 추가
    if x2-x1<=L:
        heapq.heappush(heap, x1)

    # 힙의 크기가 현재 포함된 선분의 개수
    answer = max(answer, len(heap))

print(answer)