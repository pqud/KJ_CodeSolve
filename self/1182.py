from itertools import combinations


N, S = map(int, input().split())
answer = 0

inputs = list(map(int, input().split()))

for i in range(1,N+1):
    cases= list(combinations(inputs,i))
    # print(cases)
    for case in cases:
        if sum(case)==S:
            answer+=1

print(answer)