def fact(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

n = int(input())
print(fact(n))

# 시간 복잡도는 for문을 돌리나 재귀함수나 동일하지만 공간 복잡도는 for 돌리는게 덜 잡아먹는다.