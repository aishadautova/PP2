from collections import Counter
s = list(map(str, input().split()))
s.sort()
res = set()
c = Counter(s)
for i in s:
    x = c[i]
    if x%2 == 0:
        res.add(i)

for i in res:
    print(i)