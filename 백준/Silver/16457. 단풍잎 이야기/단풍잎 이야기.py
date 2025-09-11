import sys
from itertools import combinations

input = sys.stdin.readline
# n은 키 개수, m은 퀘스트 개수, k각 퀘마다 필요한 스킬 개수
n, m, k= map(int, input().split())

quest = {}
skill=[]
answer=0

for i in range(0, m):
    need=list(map(int, input().split()))
    quest[i]=need

    for _ in need:
        skill.append(_)
    
skill=set(skill)
# print(skill)

for combi in combinations(skill, n):
    # print(combi)
    cnt=0
    for q in quest.values():
        if all(v in combi for v in q):
            cnt+=1
    
    if cnt > answer:
        answer=cnt
if n>len(skill):
    print(m)
else: 
    print(answer)