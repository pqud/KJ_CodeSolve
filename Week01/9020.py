def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


T = int(input())

for _ in range(T): 
    N=int(input())

    A, a = N // 2, N // 2
    while True:
        if is_prime(A) and is_prime(a):
            print(f"{A} {a}")
            break
        A -= 1
        a += 1

 