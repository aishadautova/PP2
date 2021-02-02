n = input()

product = 1
sm = 0
x = 0

while x < len(n):
    product *= int(n[x])
    sm += int(n[x])
    x += 1

print(product - sm)