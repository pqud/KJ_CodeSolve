import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b, u = map(int, input().split())
    graph[a].append((b, u))
    graph[b].append((a, u))

def dfs_stack(start, k):
    visited = [False] * (N+1)
    stack = []
    visited[start] = True
    count = 0

    # (현재노드, 경로상 최소 usado)
    stack.append((start, float('inf')))

    while stack:
        cur, min_usado = stack.pop()
        for nxt, usado in graph[cur]:
            if not visited[nxt]:
                next_min = min(min_usado, usado)
                if next_min >= k:
                    visited[nxt] = True
                    count += 1
                    stack.append((nxt, next_min))
                else:
                    # k 미만인 경우, 방문하지 않음
                    visited[nxt] = True  # 이 줄은 없어도 됨(트리라서)
    return count

for _ in range(Q):
    k, v = map(int, input().split())
    print(dfs_stack(v, k))
