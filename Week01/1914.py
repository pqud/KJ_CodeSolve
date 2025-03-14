import sys


# 하노이의탑은 시간복잡도가 O(2^n)이기 때문에 n의 수가 커지면 6초(10^8*6)을 얼마든지 넘을 수 있다.
# 때문에 문제에서는 21 이상의 숫자는 과정을 생략해도 된다고 되어있다.
# 또한 하노이의 탑은 최소 움직임 공식이 2^n-1으로 정해져 있다... 이를 이용한다.


sys.setrecursionlimit(10**6)  # 재귀 깊이 설정

def hanoi(n, start, sub, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, end, sub)
    print(start, end)
    hanoi(n - 1, sub, start, end)

n = int(input())

# n >= 20일 때는 O(1) 연산만 수행하여 빠르게 처리
if n > 20:
    print(2**n - 1)
else:
    print(2**n - 1)
    hanoi(n, 1, 2, 3)
