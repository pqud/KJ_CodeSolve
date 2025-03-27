import sys
import heapq


N=int(sys.stdin.readline())

under_mid=[] #최대힙
upper_mid=[] #최소힙

#최소힙 아래에 최대힙 깔아서 모래시계 모양으로 해 놓고 위아래 순서대로 넣으면 
# under_mid의 top은 중앙값이 된다!

#under_mid의 top보다 upper_mid의 top이 커야한다.
answers=[]

for i in range(1,N+1):
    value=int(sys.stdin.readline())

    if i%2==0: #짝수번째
        heapq.heappush(upper_mid, value)
        
    else:
        heapq.heappush(under_mid, -value)
    
    if upper_mid and under_mid and upper_mid[0]<-under_mid[0]:
        up=heapq.heappop(upper_mid)
        un=heapq.heappop(under_mid)

        heapq.heappush(under_mid, -up)
        heapq.heappush(upper_mid, -un)

    # print(upper_mid)
    # print(under_mid)


    # print(-under_mid[0])
    # print(f"출력: {-under_mid[0]}")
    answers.append(-under_mid[0])

for ans in answers:
    print(ans)