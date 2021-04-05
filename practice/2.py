
lines = open('text.txt').read().splitlines()

for i, l in enumerate(lines):
    pass

x = int(i)
k = 0
for _ in range(x):
    a = len(lines[_])
    b = len(lines[_+1])

    if a > b:
        print("No")
        k = 1
        break

if k == 0:
    print("Yes")