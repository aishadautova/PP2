n = list(map(int, input().split()))

k = int(input())

if k >= 0:

    for x in range(len(n)):

        z = (len(n) - k + x)%len(n)

        print(n[z], end = " ")

if k < 0:

    k = len(n) + k

    for x in range(len(n)):

        z = (len(n) - k + x)%len(n)

        print(n[z], end = " ")
