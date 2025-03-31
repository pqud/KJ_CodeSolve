#흰 방의 가중치는 0이고 검은방의 가중치는 1이라고 잡고
#그러면 진짜 그냥 다익스트라 해서 가중치 합을 출력하면 될 것 같은디?
#아니 흰방이 1이고 검은방이 0이네;;; 거꾸로인줄 문제좀잘읽자 하린아아

import sys
import heapq

dx, dy= [-1,0,1,0], [0,1,0,-1]

input=sys.stdin.readline

n= int(input())

graph=[[0] for _ in range(n)]

for i in range(n):
    row=list(''.join('1' if bit == '0' else '0' for bit in input()))
    graph[i]=row[0:-1]

distances=[[float('inf')]*(n) for _ in range(n)]

def dijkstra(graph, start):
    cx, cy= start

    distances[cx][cy]=0
    pq=[(0,cx,cy)]

    while pq:
        cur_dis, cx, cy= heapq.heappop(pq)

        if cur_dis>distances[cx][cy]: continue

        for i in range(4):
            nx, ny= cx+dx[i], cy+dy[i]

            if 0<=nx<n and 0<=ny<n:
                # print(f"cur_dis: {cur_dis}")
                # print(f"int(graph[nx][ny]): {int(graph[nx][ny])}")
                dist=int(graph[nx][ny])+cur_dis
                # print(f"nx: {nx}, ny: {ny}, dist:{dist}")
                if distances[nx][ny] > dist :
                    distances[nx][ny]=dist
                    heapq.heappush(pq, (dist, nx, ny)) 

    return distances

dijkstra(graph, (0,0))
print(distances[n-1][n-1])


