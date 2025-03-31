import sys
import heapq

input=sys.stdin.readline

N,M,K,X=map(int, input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    start,end=map(int,input().split())
    graph[start].append((end,1))

distances = [float('inf')] * (N + 1)

def djikstra(graph, start):
    distances[start] = 0
    # print(distances)

    pq=[(0,start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # print(distances[current_node])
        if current_distance> distances[current_node]: continue

        for neighbor, weight in graph[current_node]:
            distance=current_distance+weight
        
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(pq, (distance, neighbor))

    return distances
    
djikstra(graph, X)

# print(distances)

cnt=0
for i in range(len(distances)):
    if distances[i]==K:
        print(i)
        cnt+=1

    if i==len(distances)-1 and distances[i]!=K and cnt==0:
        print(-1)
