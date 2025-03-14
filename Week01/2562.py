a = [int(input()) for _ in range(9)]

number=0
index=0

for i in range(9):
    if number < a[i]:
        number = a[i]
        index=i+1

print(number)
print(index)