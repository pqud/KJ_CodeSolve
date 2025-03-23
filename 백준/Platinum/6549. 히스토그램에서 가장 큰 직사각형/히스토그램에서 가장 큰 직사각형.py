import sys

def largestRectangleArea(heights):
    n = len(heights)
    if n == 0:
        return 0
    
    nodes = [[h, i, i, ''] for i, h in enumerate(heights)]  # [높이, l, r, rl]
    max_area = 0
    
    # Step 1: rl 값 설정
    for i in range(1, n-1):
        if heights[i-1] > heights[i+1]:
            nodes[i][3] = 'l'
        else:
            nodes[i][3] = 'r'
    
    # Step 2: l과 r 설정 (왼쪽/오른쪽 확장 범위)
    for i in range(n):
        while nodes[i][1] > 0 and heights[nodes[i][1] - 1] >= nodes[i][0]:
            nodes[i][1] = nodes[nodes[i][1] - 1][1]  # 왼쪽 확장
    
    for i in range(n-1, -1, -1):
        while nodes[i][2] < n-1 and heights[nodes[i][2] + 1] >= nodes[i][0]:
            nodes[i][2] = nodes[nodes[i][2] + 1][2]  # 오른쪽 확장
    
    # Step 3: 병합하면서 최대 넓이 갱신
    for i in range(n):
        width = nodes[i][2] - nodes[i][1] + 1
        max_area = max(max_area, width * nodes[i][0])
    
    return max_area

# 예제 실행
while True:
    heights=list(map(int, sys.stdin.readline().split()))
    if heights[0]==0:
        break
    print(largestRectangleArea(heights[1:]))  # 결과: 10