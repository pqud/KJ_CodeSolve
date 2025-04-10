import sys
import heapq

input=sys.stdin.readline

lectures=[]

n=int(input())
for i in range(n):
    id, start, end = map(int, input().split())
    lectures.append([id, start, end])

lectures.sort(key=lambda x: (x[1],x[2],[0]))

space=[[0,1]] #각 빈 강의실 [종료시간, 강의실 번호 ]
room_cnt=1
result=[1]*n


for lec_id, start, end in lectures:
    if space[0][0] <= start:
        finish, room_id= heapq.heappop(space)
    else: #새 강의실 필요함
        room_cnt+=1
        room_id=room_cnt
    heapq.heappush(space, (end, room_id))
    result[lec_id-1]=room_id


print(room_cnt)
for room in result:
    sys.stdout.write(f"{room}\n")

