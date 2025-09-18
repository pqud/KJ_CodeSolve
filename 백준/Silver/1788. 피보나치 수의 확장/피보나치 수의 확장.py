n = int(input())

if n == 0:
    print(0)
    print(0)
else:
    a, b = 0, 1
    for _ in range(abs(n)):
        a, b = b, (a + b) % 1000000000  # 1e9 나머지 연산
    if n < 0 and abs(n) % 2 == 0:
        print(-1)
    else:
        print(1)
    print(a)
