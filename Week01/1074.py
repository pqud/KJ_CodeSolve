N, r, c = map(int, input().split())

answer = 0

def find_Area(N, r, c):
    global answer

    if N == 0:
        return
    
    size = 2**(N-1)  # 현재 분할 크기 (사분면의 한 변 길이)
    
    # 몇 번째 사분면인지 확인
    if r < size and c < size:  # 0번 사분면 (좌상단)
        num = 0
    elif r < size and c >= size:  # 1번 사분면 (우상단)
        num = 1
        c -= size  # 다음 좌표 변환
    elif r >= size and c < size:  # 2번 사분면 (좌하단)
        num = 2
        r -= size  # 다음 좌표 변환
    else:  # 3번 사분면 (우하단)
        num = 3
        r -= size
        c -= size

    answer += (size * size) * num  # 이전 방문 수 누적
    find_Area(N-1, r, c)  # 더 작은 크기로 재귀 호출

find_Area(N, r, c)
print(answer)
