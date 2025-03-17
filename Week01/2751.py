import random

def partition(data, start, end):
    pivot = random.randint(start, end)  # 무작위 피벗 선택
    data[start], data[pivot] = data[pivot], data[start]  # 피벗을 첫 번째로 교환
    pivot = start
    i = start + 1
    j = end
    done = False

    while not done:
        while i <= end and data[i] < data[pivot]:  # 좌 -> 우, 피벗보다 큰 값 찾기
            i += 1
        while j > start and data[j] > data[pivot]:  # 우 -> 좌, 피벗보다 작은 값 찾기
            j -= 1
        if j < i:  # i와 j가 엇갈린 경우 종료
            done = True
        else:
            data[i], data[j] = data[j], data[i]

    data[pivot], data[j] = data[j], data[pivot]  # 피벗과 j의 값 교환
    return j

def quick_sort(data, start, end):
    stack = []
    stack.append(start)
    stack.append(end)

    while stack:
        end = stack.pop()
        start = stack.pop()
        if start >= end:  #start와 end 같은 값이면 1개짜리 배열이라 정렬 끝난 상황이고 start>end면 잘못된 구간이다.
            continue
        pivot = partition(data, start, end)

        if pivot - 1 > start:  # 피벗 왼쪽으로 분할 가능
            stack.append(start)
            stack.append(pivot - 1)

        if pivot + 1 < end:  # 피벗 오른쪽으로 분할 가능
            stack.append(pivot + 1)
            stack.append(end)

if __name__ == "__main__":
    N = int(input())
    data = [int(input()) for _ in range(N)]  # 리스트 컴프리헨션으로 입력 받기

    quick_sort(data, 0, N - 1)

    print("\n".join(map(str, data)))  # 빠른 출력
