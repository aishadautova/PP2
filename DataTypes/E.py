k, n = input().split()
k = int(k)
n = int(n)

p = n // k

s = n % k

x = (n - (n // k) * k) % (s - 1)

print(x)