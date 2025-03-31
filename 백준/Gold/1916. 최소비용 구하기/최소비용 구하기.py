import sys
import heapq

input=sys.stdin.readline

N=int(input())
M=int(input())

graph=[[] for _ in range(N+1)] 


for i in range(M):
    start, end, weight=map(int,input().split())
    graph[start].append((end,weight))

tar_start, tar_end=map(int, input().split())
    
distances=[float('inf')] * (N+1)

def dijkstra(graph, start):
    distances[start]=0
    pq=[(0, start)]

    while pq:
        cur_dis, cur_node=heapq.heappop(pq)

        if cur_dis> distances[cur_node]: continue

        for neig, weight in graph[cur_node]:
            dist=cur_dis+weight

            if dist<distances[neig]:
                distances[neig]=dist
                heapq.heappush(pq, (dist, neig))

    return distances

dijkstra(graph, tar_start)

print(distances[tar_end])

