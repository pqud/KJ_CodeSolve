import sys


N = int(sys.stdin.readline().strip())

dots = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

dots.sort()

def find_min(left, right):

    if right==left:
        return float('inf')
    
    if right-left==1: #점이 두개뿐임
        return (dots[right][0]-dots[left][0])**2 + (dots[right][1]-dots[left][1])**2
    
    #왼쪽 또는 오른쪽에 있는 값값
    mid=(left+right)//2
    mid_x=dots[mid][0]

    ans=min(find_min(left,mid),find_min(mid+1, right))

    #경계선 근처 점들을 모으기
    temp=[]
    for i in range(left, right+1):
        if(dots[i][0] - mid_x )**2<ans:
            temp.append(dots[i])

    temp.sort(key=lambda p: p[1]) #y 값 기준으로 정렬렬

    # 경계선 근처 점들끼리 모아서 비교함. 그 거리값이 ans보다 크면 필요없음
    for i in range(len(temp)):
        for j in range(i+1, len(temp)):
            if (temp[j][1] - temp[i][1]) ** 2 >=ans: 
                break
            ans=min(ans, (temp[i][0]-temp[j][0])**2 + (temp[i][1]-temp[j][1])**2)
 
    return ans


print(find_min(0,N-1))