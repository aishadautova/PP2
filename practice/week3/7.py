set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
y = set1
x = set1.difference(set2)
res = y - x
print(len(res))
