# 문서 중요도 받을 때 내림차순으로 정렬하고 그거랑 동일한 값이 나올때까지 popleft/push 하면 될듯


import sys
from collections import deque

T=int(sys.stdin.readline())
for i in range(T):
    N, which=map(int, sys.stdin.readline().split())

    priority=list(map(int, sys.stdin.readline().split()))
    papers=[[x, priority[x]] for x in range(0, N)]
    papers=deque(papers)

    priority.sort(reverse=True)
    # print(papers.popleft())

    for j in range(N):
        while True:
            front=papers.popleft()
            if front[1]==priority[j]:
                if front[0]==which:
                    print(j+1)
                break
            else: #앞에꺼 뽑아다 뒤에다 삽입
                papers.append(front)


