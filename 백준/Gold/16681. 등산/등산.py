import sys
import heapq

input = sys.stdin.readline

N, M, D, E = map(int, input().split())
heights= list(map(int, input().split()))
nodes=[ [] for _ in range(N+1)]

for _ in range(M):
    start, end, dis= map(int, input().split())
    nodes[start].append([end, dis])
    nodes[end].append([start, dis])


dist_from_start=[float('inf')]*(N+1)
dist_from_k=[float('inf')]*(N+1)


def dijkstra(dist, start):
    dist[start] = 0
    pq = [(0, start)]  # (거리, 노드)

    while pq:
        cur_dis, cur_node = heapq.heappop(pq)
        if cur_dis > dist[cur_node]:
            continue

        for neighbor, weight in nodes[cur_node]:
            # 높이 조건: neighbor가 더 높아야 이동 가능
            if heights[cur_node-1] < heights[neighbor-1]:
                distance = cur_dis + weight
                if distance < dist[neighbor]:
                    dist[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

    return dist


dijkstra(dist_from_start, 1)
dijkstra(dist_from_k, N)

answer = float('-inf')

for i in range(2, N+1):
    if dist_from_start[i] != float('inf') and dist_from_k[i] != float('inf'):
        value = heights[i-1]*E - (dist_from_start[i] + dist_from_k[i])*D
        answer = max(answer, value)

print(answer if answer != float('-inf') else "Impossible")