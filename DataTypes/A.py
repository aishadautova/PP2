n, m = input().split()
m = int(m)
n = int(n)

if n >= m:
    print(1)
elif(m % n == 0):
    print(m // n)
else:
    print(m // n + 1)