n = list(map(int, input().split()))

min = 1001

for x in n:
    if x > 0:
        if x < min:
            min = x

print(min)
