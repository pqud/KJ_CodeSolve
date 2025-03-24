import sys

def largestRectangleArea(heights, L):
    stack = []  # (인덱스, 높이)
    max_size = 0

    for i in range(L):
        while stack and stack[-1][1] > heights[i]: #스택 꼭대기의 블록의 높이가 새 블록보다 크면면
            top = stack.pop()
            width = i if not stack else i - stack[-1][0] - 1 #가로길이는 스택이 비지 않았다면 i 스택이 비었으면 i-꼭대기 블록의 인덱스  
            max_size = max(max_size, top[1] * width) 
        stack.append((i, heights[i]))

    while stack: #스택이 빌 때 까지(위의 루프 다 돌고나서 아직 계산하지 않은 히스토그램 있음)
        top = stack.pop() 
        width = L if not stack else L - stack[-1][0] - 1 #가로길이는 스택이 비지 않았다면 L 비었으면 L-꼭대기 블록의 인덱스
        max_size = max(max_size, top[1] * width)

    return max_size

while True:
    heights = list(map(int, sys.stdin.readline().split()))
    if heights[0] == 0:
        break

    result = largestRectangleArea(heights[1:], heights[0])
    print(result)
