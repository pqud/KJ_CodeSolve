def permutations_2(array, r):
    for i in range(len(array)):
        if r == 1:
            return [array[i]]
        else:
            for next in permutations_2(array[:i]+array[i+1:], r-1):
                return [array[i]] + next

array = [1, 2, 3]
r = 2

for perm in permutations_2(array, r):
    print(perm)